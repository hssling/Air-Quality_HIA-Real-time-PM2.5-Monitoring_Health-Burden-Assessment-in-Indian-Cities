import streamlit as st
import pandas as pd
import plotly.express as px
import glob
from pathlib import Path

st.set_page_config(
    page_title="Air Quality and Health Dashboard",
    layout="wide"
)
BASE = Path("projects/air_quality_health")

st.title("🌫 Air Quality & Health Impact")

# latest PM2.5
files = sorted(glob.glob(str(BASE / "data" / "openaq" / "openaq_pm25_IN_*.csv")))
if not files:
    st.warning("Run fetch_openaq.py first.")
else:
    df = pd.read_csv(files[-1])
    st.subheader("PM2.5 Measurements (OpenAQ)")
    city_mean = df.groupby("city")["value"].mean().reset_index()
    fig = px.bar(
        city_mean.sort_values("value", ascending=False).head(20),
        x="value",
        y="city",
        orientation="h",
        title="Top 20 Cities by Mean PM2.5 (µg/m³)"
    )
    st.plotly_chart(fig, use_container_width=True)

# WHO deaths
try:
    who = pd.read_csv(BASE / "data" / "who" / "air_pollution_death_rate.csv")
    latest = who.groupby("country").last().reset_index()
    fig2 = px.choropleth(
        latest,
        locations="country",
        locationmode="country names",
        color="death_rate",
        title="Air Pollution Death Rate (per 100k, IHME)",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig2, use_container_width=True)
except Exception:
    st.info("WHO/IHME data not yet downloaded.")
