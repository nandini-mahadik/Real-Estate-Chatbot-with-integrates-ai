from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import pandas as pd
import os
from django.conf import settings

from .excel_loader import (
    load_df, 
    filter_by_area, 
    filter_multiple_areas, 
    get_trend_for_area
)

from .chatbot import (
    analyze_single_area,
    analyze_multi_area,
    create_ai_summary
)


# =========================================================
# ===============  MAIN ANALYZE API  ======================
# =========================================================
@api_view(["POST"])
def analyze(request):
    """
    Handles:
    - Analyze Wakad
    - Compare Baner and Aundh
    """
    query = request.data.get("query", "").strip().lower()
    df = load_df()

    print("COLUMNS:", df.columns.tolist())

    if not query:
        return Response({"error": "Query is required"}, status=400)

    # ---------------------------------------------------------
    # MULTI-AREA COMPARISON
    # ---------------------------------------------------------
    if "compare" in query:
        cleaned = query.replace("compare", "")
        parts = [p.strip() for p in cleaned.replace("and", ",").split(",") if p.strip()]

        if len(parts) >= 2:
            df_filtered = filter_multiple_areas(parts)

            # Catch empty comparison
            if df_filtered.empty:
                return Response({"error": "No matching areas found"}, status=404)

            # Basic summary for internal use
            _ = analyze_multi_area(parts, df)

            # AI summary
            try:
                ai_summary = create_ai_summary(query, df_filtered.head().to_dict(orient="records"))
            except Exception as e:
                ai_summary = f"[AI Summary Error: {e}]"

            return Response({
                "summary": ai_summary,
                "trend": {area: get_trend_for_area(area) for area in parts},
                "table": df_filtered.to_dict(orient="records")
            })

    # ---------------------------------------------------------
    # SINGLE AREA QUERY
    # ---------------------------------------------------------
    area_name = query.replace("analyze", "").strip()
    df_area = filter_by_area(area_name)

    if not df_area.empty:

        # Basic non-AI summary
        _ = analyze_single_area(area_name, df_area)

        # AI summary
        try:
            ai_summary = create_ai_summary(query, df_area.head().to_dict(orient="records"))
        except Exception as e:
            ai_summary = f"[AI Summary Error: {e}]"

        trend = get_trend_for_area(area_name)
        table = df_area.to_dict(orient="records")

        print("TREND DATA:", trend)

        return Response({
            "summary": ai_summary,
            "trend": trend,
            "table": table
        })

    return Response({"error": "Area not found in dataset"}, status=404)



# =========================================================
# ===============  DOWNLOAD EXCEL API  ====================
# =========================================================
@api_view(["POST"])
def download_excel(request):
    rows = request.data.get("rows", [])

    if not rows:
        return Response({"error": "No rows provided"}, status=400)

    df = pd.DataFrame(rows)

    # Save the file temporarily
    file_path = os.path.join(settings.BASE_DIR, "filtered_data.xlsx")
    df.to_excel(file_path, index=False)

    # Send file to frontend
    with open(file_path, "rb") as f:
        response = HttpResponse(f.read(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment; filename=filtered_data.xlsx"
        return response
