import subprocess
import sys
from pathlib import Path

def run(c):
    print("==>", c)
    r = subprocess.run(c, shell=True)
    if r.returncode != 0:
        sys.exit(r.returncode)

print("🔬 Running Extended Analysis (Time-series + Regression)")
print("=" * 55)

# Use the virtual environment Python executable
python_exe = Path(".venv/Scripts/python.exe").resolve()

run(f'"{python_exe}" projects/air_quality_health/scripts/decompose_pm25.py')
run(f'"{python_exe}" projects/air_quality_health/scripts/regress_pm25_mortality.py')

print("🎯 Extended analyses complete!")
print("📈 Check outputs/plots & outputs/tables/")
print("🌐 Super Dashboard: streamlit run projects/air_quality_health/dashboards/app_super.py")
