import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import glob
from pathlib import Path

st.set_page_config(
    page_title="Air Quality & Health Super-Dashboard",
    layout="wide"
)
BASE = Path("projects/air_quality_health")

st.title("🌫 Air Quality & Health — Integrated Analytics Dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Current PM₂․₅",
    "📈 Trends & Decomposition",
    "🔮 Forecast (Prophet)",
    "⚕️ Regression & Health Impact"
])

# -------------- TAB 1 – Current PM₂․₅ --------------
with tab1:
    st.subheader("Real-time PM₂․₅ from OpenAQ")
    files = sorted(glob.glob(str(BASE / "data" / "openaq" / "openaq_pm25_IN_*.csv")))
    if not files:
        st.warning("Run fetch_openaq.py first.")
    else:
        df = pd.read_csv(files[-1])
        city_mean = df.groupby("city")["value"].mean().reset_index()
        fig = px.bar(
            city_mean.sort_values("value", ascending=False).head(20),
            x="value",
            y="city",
            orientation="h",
            title="Top 20 Cities by Mean PM₂․₅ (µg/m³)"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(
            "National Average PM₂․₅ (µg/m³)",
            f"{city_mean['value'].mean():.1f}"
        )

# -------------- TAB 2 – Trends & Decomposition --------------
with tab2:
    st.subheader("Seasonal Decomposition (7-day period)")
    trend_files = sorted(glob.glob(str(BASE / "outputs" / "tables" / "trend_*.csv")))
    if not trend_files:
        st.info("Run decompose_pm25.py first.")
    else:
        cities = sorted([
            Path(f).stem.replace("trend_", "").replace("_", " ")
            for f in trend_files
        ])
        city = st.selectbox("Select city to view trend", cities)
        fpath = BASE / "outputs" / "tables" / f"trend_{city.replace(' ', '_')}.csv"
        df = pd.read_csv(fpath)
        fig = px.line(df, x="date", y="trend", title=f"PM₂․₅ Trend for {city}")
        st.plotly_chart(fig, use_container_width=True)

# -------------- TAB 3 – Forecast (Prophet) --------------
with tab3:
    st.subheader("30-day Forecast of PM₂․₅")
    forecast_files = sorted(glob.glob(str(BASE / "outputs" / "tables" / "forecast_*.csv")))
    if not forecast_files:
        st.info("Run forecast_pm25.py first.")
    else:
        cities = sorted([
            Path(f).stem.replace("forecast_", "").replace("_", " ")
            for f in forecast_files
        ])
        city = st.selectbox("Choose city for forecast", cities)
        fpath = BASE / "outputs" / "tables" / f"forecast_{city.replace(' ', '_')}.csv"
        df = pd.read_csv(fpath)
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df["ds"],
            y=df["yhat"],
            mode="lines",
            name="Forecast"
        ))
        fig.add_trace(go.Scatter(
            x=df["ds"],
            y=df["yhat_upper"],
            mode="lines",
            line=dict(width=0),
            name="Upper CI"
        ))
        fig.add_trace(go.Scatter(
            x=df["ds"],
            y=df["yhat_lower"],
            mode="lines",
            fill="tonexty",
            name="Lower CI"
        ))
        fig.update_layout(
            title=f"Predicted PM₂․₅ — {city}",
            xaxis_title="Date",
            yaxis_title="µg/m³"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(
            df[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30),
            use_container_width=True
        )

# -------------- TAB 4 – Regression & Health Impact --------------
with tab4:
    st.subheader("Regression Results — PM₂․₅ vs Mortality Rates")
    reg_path = BASE / "outputs" / "tables" / "pm25_mortality_regression.txt"
    fe_path = BASE / "outputs" / "tables" / "pm25_mortality_fixed_effects.txt"
    if not reg_path.exists():
        st.info("Run regress_pm25_mortality.py first.")
    else:
        st.text("OLS Regression Summary:")
        st.code(reg_path.read_text())
    if fe_path.exists():
        st.text("Fixed Effects Panel Model:")
        st.code(fe_path.read_text())
