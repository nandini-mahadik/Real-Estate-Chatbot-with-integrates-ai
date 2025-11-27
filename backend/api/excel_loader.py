import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "dataset.xlsx")

_df_cache = None


def load_df():
    global _df_cache
    if _df_cache is None:
        df = pd.read_excel(DATA_PATH)

        # Normalize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # ---- AREA ----
        if "final location" in df.columns:
            df["area"] = df["final location"]
        else:
            raise ValueError("Missing column: final location")

        # ---- YEAR ----
        if "year" not in df.columns:
            raise ValueError("Missing column: year")

        # ---- PRICE (weighted avg of all types) ----
        price_cols = [
            "flat - weighted average rate",
            "office - weighted average rate",
            "others - weighted average rate",
            "shop - weighted average rate",
        ]
        price_cols = [c for c in price_cols if c in df.columns]

        if len(price_cols) > 0:
            df["price"] = df[price_cols].mean(axis=1)
        else:
            df["price"] = 0  # fallback

        # ---- DEMAND (total sales + total sold) ----
        demand_cols = ["total_sales - igr", "total sold - igr"]
        demand_cols = [c for c in demand_cols if c in df.columns]

        if len(demand_cols) > 0:
            df["demand"] = df[demand_cols].sum(axis=1)
        else:
            df["demand"] = 0

        # ---- SIZE ----
        if "total carpet area supplied (sqft)" in df.columns:
            df["size"] = df["total carpet area supplied (sqft)"]
        else:
            df["size"] = 0

        # ---- Final cleaned dataframe ----
        df = df[["area", "year", "price", "demand", "size"]]

        _df_cache = df

    return _df_cache


def filter_by_area(area):
    df = load_df()
    return df[df["area"].str.lower() == area.lower().strip()]


def filter_multiple_areas(area_list):
    df = load_df()
    area_list = [a.lower().strip() for a in area_list]
    return df[df["area"].str.lower().isin(area_list)]


def get_trend_for_area(area):
    df = load_df()

    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Should match: area, year, price, demand, size
    if not all(col in df.columns for col in ["area", "year", "price", "demand"]):
        print("❌ Trend Error: Required columns missing:", df.columns.tolist())
        return []

    # Filter area
    df_area = df[df["area"].str.lower() == area.lower()]

    if df_area.empty:
        print("❌ Trend Error: No matching area:", area)
        return []

    # Generate the trend
    trend = (
        df_area.groupby("year")[["price", "demand"]]
        .mean()
        .reset_index()
        .sort_values("year")
    )

    trend_json = trend.to_dict(orient="records")

    print("✅ Trend Output:", trend_json)  # <-- IMPORTANT
    return trend_json
