import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from pathlib import Path
from tqdm import tqdm
import glob

BASE = Path("projects/air_quality_health")
DATA = BASE / "data" / "openaq"
OUTT = BASE / "outputs" / "tables"
OUTP = BASE / "outputs" / "plots"
OUTT.mkdir(parents=True, exist_ok=True)
OUTP.mkdir(parents=True, exist_ok=True)

# find latest OpenAQ file
files = sorted(glob.glob(str(DATA / "openaq_pm25_IN_*.csv")))
if not files:
    raise SystemExit("⚠ No OpenAQ PM2.5 file found. Run fetch_openaq.py first.")

df = pd.read_csv(files[-1])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
daily = df.groupby(["city", "date"])["value"].mean().reset_index()

for city, group in tqdm(daily.groupby("city")):
    if len(group) < 14:
        continue
    g = group.rename(columns={"date": "ds", "value": "y"})
    model = Prophet(
        seasonality_mode="additive",
        yearly_seasonality=False,
        weekly_seasonality=True,
        daily_seasonality=False
    )
    model.fit(g)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    # plot
    fig = model.plot(forecast)
    plt.title(f"PM2.5 Forecast (next 30 days) — {city}")
    plt.tight_layout()
    out_plot = OUTP / f"forecast_{city.replace(' ', '_')}.png"
    plt.savefig(out_plot)
    plt.close()
    # save forecast CSV
    forecast["city"] = city
    forecast.to_csv(OUTT / f"forecast_{city.replace(' ', '_')}.csv", index=False)

print("✅ Forecasts and plots generated for each city (30 days ahead).")
