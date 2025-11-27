import os
import pandas as pd
from groq import Groq

# Load environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

client = Groq(api_key=GROQ_API_KEY)

# ---------------- SINGLE AREA ANALYSIS ----------------
def analyze_single_area(area, df_area):
    """
    df_area has columns: area, year, price, demand, size
    """
    avg_price = df_area["price"].mean()
    avg_demand = df_area["demand"].mean()
    avg_size = df_area["size"].mean()

    years = sorted(df_area["year"].unique())

    return {
        "area": area,
        "avg_price": float(avg_price),
        "avg_demand": float(avg_demand),
        "avg_size": float(avg_size),
        "years": years
    }

# ---------------- MULTIPLE AREA ANALYSIS ----------------
def analyze_multi_area(areas, df):
    output = []

    for area in areas:
        df_area = df[df["area"].str.lower() == area.lower()]
        if df_area.empty:
            continue

        avg_price = df_area["price"].mean()
        avg_demand = df_area["demand"].mean()

        output.append({
            "area": area,
            "avg_price": float(avg_price),
            "avg_demand": float(avg_demand),
        })

    return output

# ---------------- AI SUMMARY (GROQ) ----------------
def create_ai_summary(query, data_dict):
    """
    Uses Groq LLM to generate a clean, short summary.
    """
    try:
        prompt = f"""
You are a real estate analysis expert.
User asked: "{query}"

Dataset summary:
{data_dict}

Write a clear, 5–7 sentence insight focusing on:
• price trends
• demand patterns
• area comparison
Avoid unnecessary text.
"""

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        # FIX: Groq uses .content, not ["content"]
        return response.choices[0].message.content

    except Exception as e:
        return f"No AI summary available due to: {str(e)}"
