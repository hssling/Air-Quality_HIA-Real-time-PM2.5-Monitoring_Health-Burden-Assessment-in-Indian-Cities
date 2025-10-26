import subprocess
import sys
from pathlib import Path

def run(c):
    print("==>", c)
    r = subprocess.run(c, shell=True)
    if r.returncode != 0:
        sys.exit(r.returncode)

print("🚀 Starting Air Quality & Health Analysis Pipeline")
print("=" * 50)

# Use the virtual environment Python executable
python_exe = Path(".venv/Scripts/python.exe").resolve()

run(f'"{python_exe}" projects/air_quality_health/scripts/fetch_openaq.py')
run(f'"{python_exe}" projects/air_quality_health/scripts/load_health_data.py')
run(f'"{python_exe}" projects/air_quality_health/scripts/analyze_data.py')
run(f'"{python_exe}" projects/air_quality_health/scripts/make_report.py')

print("🎉 Basic analysis complete!")
print("📊 Dashboard: streamlit run projects/air_quality_health/dashboards/app.py")
print("🔬 Extended analysis: python projects/air_quality_health/run_extended.py")
print("🔮 Forecasting: python projects/air_quality_health/run_forecast.py")
