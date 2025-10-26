import pandas as pd
from pathlib import Path
import numpy as np

BASE = Path("projects/air_quality_health")
DATA = BASE / "data" / "who"
DATA.mkdir(parents=True, exist_ok=True)

def load_who_sample():
    """
    Generate sample health impact data since the original WHO/IHME URL is not available.
    This creates realistic synthetic data for demonstration purposes.
    """
    print("⚠ WHO/IHME URL not available, generating sample health data...")

    # Countries with realistic air pollution death rates (per 100,000 population)
    countries_data = {
        "India": 98.5,
        "China": 89.2,
        "Pakistan": 95.8,
        "Bangladesh": 102.3,
        "Indonesia": 67.4,
        "Nigeria": 45.6,
        "United States": 12.8,
        "Brazil": 23.4,
        "Russia": 35.7,
        "Japan": 8.9,
        "Germany": 15.2,
        "United Kingdom": 11.7,
        "France": 13.8,
        "Italy": 18.9,
        "Spain": 16.3,
        "Canada": 9.2,
        "Australia": 7.8,
        "South Korea": 22.1,
        "Mexico": 28.7,
        "South Africa": 42.3,
        "Egypt": 78.9,
        "Turkey": 34.5,
        "Thailand": 45.6,
        "Vietnam": 52.1,
        "Philippines": 38.9,
        "Iran": 65.4,
        "Saudi Arabia": 29.8,
        "Argentina": 19.7,
        "Colombia": 25.3,
        "Poland": 41.2
    }

    # Generate time series data from 2000 to 2019
    data_rows = []
    for year in range(2000, 2020):
        for country, base_rate in countries_data.items():
            # Add trend (slight improvement over time) and variation
            trend_factor = 1.0 - (year - 2000) * 0.015  # 1.5% annual improvement
            variation = np.random.normal(0, base_rate * 0.1)  # 10% variation
            death_rate = max(1, base_rate * trend_factor + variation)

            data_rows.append({
                "country": country,
                "year": year,
                "death_rate": round(death_rate, 1)
            })

    df = pd.DataFrame(data_rows)

    # Save to CSV
    df.to_csv(DATA / "air_pollution_death_rate.csv", index=False)
    print(f"✅ Generated sample health data with {len(df)} records saved.")
    print(f"🌍 Countries covered: {len(countries_data)}")
    print(f"📅 Years covered: 2000-2019")

    return df

if __name__ == "__main__":
    load_who_sample()
