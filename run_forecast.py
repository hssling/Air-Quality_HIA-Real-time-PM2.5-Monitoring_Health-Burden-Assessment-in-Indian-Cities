import subprocess
import sys
from pathlib import Path

def run(c):
    print("==>", c)
    r = subprocess.run(c, shell=True)
    if r.returncode != 0:
        sys.exit(r.returncode)

print("🔮 Running PM2.5 Forecasting with Prophet")
print("=" * 45)

# Use the virtual environment Python executable
python_exe = Path(".venv/Scripts/python.exe").resolve()

run(f'"{python_exe}" projects/air_quality_health/scripts/forecast_pm25.py')

print("🎯 Forecast generation complete!")
print("📊 See outputs/plots & outputs/tables/")
print("🔮 Forecast Dashboard: streamlit run projects/air_quality_health/dashboards/app_forecast.py")
