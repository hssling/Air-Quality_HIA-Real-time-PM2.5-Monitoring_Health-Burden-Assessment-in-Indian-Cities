#!/usr/bin/env python3
"""
Deployment script for Air Quality Health Analysis Dashboard
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description=""):
    """Run a command and handle errors"""
    print(f"🔄 {description}")
    print(f"   Command: {command}")

    try:
        result = subprocess.run(
            command, shell=True, check=True,
            capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"   Error: {e}")
        print(f"   stderr: {e.stderr}")
        return None


def main():
    """Main deployment function"""
    print("🚀 Air Quality Health Analysis - Deployment Script")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("streamlit_config.toml").exists():
        print("❌ Error: streamlit_config.toml not found. "
              "Are you in the project directory?")
        sys.exit(1)

    # Install dependencies
    print("\n📦 Installing dependencies...")
    run_command("pip install -r requirements.txt",
                "Installing Python dependencies")

    # Create necessary directories
    print("\n📁 Creating directories...")
    for directory in [
        "data/openaq", "data/who", "outputs/plots",
        "outputs/tables", "outputs/reports"
    ]:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   Created: {directory}")

    # Run the analysis pipeline
    print("\n🔬 Running analysis pipeline...")
    run_command("python run_all.py", "Running complete analysis pipeline")

    # Test dashboard locally
    print("\n🖥️  Testing dashboard...")
    print("   Starting dashboard on port 8501...")
    print("   Press Ctrl+C to stop the dashboard")
    print("   Dashboard URL: http://localhost:8501")

    try:
        subprocess.run(
            "streamlit run dashboards/app.py "
            "--server.config streamlit_config.toml",
            shell=True
        )
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")

    print("\n✅ Deployment completed successfully!")
    print("\n📋 Next steps:")
    print("   1. Push to GitHub: git add . && git commit -m "
          "'Deploy air quality dashboard' && git push")
    print("   2. Deploy to Streamlit Cloud or other platform")
    print("   3. Set up automated CI/CD pipeline")


if __name__ == "__main__":
    main()
