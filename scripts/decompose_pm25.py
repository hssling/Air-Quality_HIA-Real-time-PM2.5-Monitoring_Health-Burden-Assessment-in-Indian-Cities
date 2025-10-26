import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path
from tqdm import tqdm
import glob

BASE = Path("projects/air_quality_health")
DATA = BASE / "data" / "openaq"
OUTP = BASE / "outputs" / "plots"
OUTT = BASE / "outputs" / "tables"
OUTP.mkdir(parents=True, exist_ok=True)
OUTT.mkdir(parents=True, exist_ok=True)

# load latest OpenAQ file
files = sorted(glob.glob(str(DATA / "openaq_pm25_IN_*.csv")))
if not files:
    raise SystemExit("⚠ No OpenAQ data found. Run fetch_openaq.py first.")

df = pd.read_csv(files[-1])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
daily = df.groupby(["city", "date"])["value"].mean().reset_index()

for city, group in tqdm(daily.groupby("city")):
    if len(group) < 14:  # need at least 2 weeks for decomposition
        continue
    g = group.set_index("date").asfreq("D").interpolate()
    result = seasonal_decompose(g["value"], model="additive", period=7)
    fig = result.plot()
    fig.suptitle(f"Seasonal Decomposition of PM2.5 — {city}")
    plt.tight_layout()
    out = OUTP / f"decompose_{city.replace(' ', '_')}.png"
    plt.savefig(out)
    plt.close()
    # save trend for aggregation
    trend_df = result.trend.dropna().reset_index()
    trend_df.columns = ["date", "trend"]
    trend_df["city"] = city
    trend_df.to_csv(OUTT / f"trend_{city.replace(' ', '_')}.csv", index=False)

print("✅ decomposition plots & trends saved in outputs/plots and outputs/tables")
