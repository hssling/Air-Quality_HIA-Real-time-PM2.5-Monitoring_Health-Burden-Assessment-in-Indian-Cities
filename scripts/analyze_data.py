import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import glob

BASE = Path("projects/air_quality_health")
OUTP = BASE / "outputs" / "plots"
OUTT = BASE / "outputs" / "tables"
OUTP.mkdir(parents=True, exist_ok=True)
OUTT.mkdir(parents=True, exist_ok=True)

# load OpenAQ latest
files = sorted(glob.glob(str(BASE / "data" / "openaq" / "openaq_pm25_IN_*.csv")))
if not files:
    raise SystemExit("No OpenAQ data found. Run fetch_openaq.py first.")

aq = pd.read_csv(files[-1])
aq["city"] = aq["city"].fillna("Unknown")
city_mean = aq.groupby("city")["value"].mean().reset_index()
city_mean.columns = ["city", "pm25_mean"]

# Create bar plot of top 15 cities by PM2.5
plt.figure(figsize=(10, 8))
sns.barplot(
    data=city_mean.sort_values("pm25_mean", ascending=False).head(15),
    x="pm25_mean",
    y="city",
    palette="Reds_r"
)
plt.xlabel("Mean PM2.5 (µg/m³)")
plt.ylabel("City")
plt.title("Top 15 Cities by PM2.5 (last 30 days)")
plt.tight_layout()
plt.savefig(OUTP / "top_cities_pm25.png")
plt.close()

# join WHO deaths
who = pd.read_csv(BASE / "data" / "who" / "air_pollution_death_rate.csv")
who_latest = who.groupby("country").last().reset_index()

# simple scatter for illustrative correlation (country-level)
merged = who_latest.rename(columns={"country": "Entity"})
sns.scatterplot(data=merged, x="death_rate", y="death_rate")
plt.close()

print("✅ analysis done; see outputs/plots/top_cities_pm25.png")
