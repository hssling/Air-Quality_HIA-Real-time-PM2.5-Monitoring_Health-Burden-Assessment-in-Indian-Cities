# 🌫 Air Quality and Health Impact Analysis

A comprehensive research project analyzing the relationship between PM2.5 air pollution and health impacts across Indian cities using real-time data from OpenAQ and mortality data from WHO/IHME.

## 📋 Overview

This project provides:
- **Real-time PM2.5 monitoring** from OpenAQ API
- **Health impact analysis** using WHO/IHME mortality data
- **Time-series decomposition** of air quality patterns
- **Regression modeling** of pollution-health relationships
- **30-day forecasting** using Prophet
- **Interactive dashboards** for data visualization
- **Comprehensive manuscript** with full methodology and results

## 🚀 Quick Start

### 1. Setup Environment
```bash
cd projects/air_quality_health
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Run Complete Analysis
```bash
python run_all.py
```

### 3. Launch Dashboards
```bash
# Basic dashboard
streamlit run dashboards/app.py

# Super dashboard (all features)
streamlit run dashboards/app_super.py

# With custom config
streamlit run dashboards/app.py --server.config streamlit_config.toml
```

## 🚀 Deployment

### Local Deployment
```bash
# One-click deployment
python deploy.py

# Or manually:
python run_all.py
streamlit run dashboards/app.py --server.config streamlit_config.toml
```

### Production Deployment

#### Option 1: Streamlit Cloud
1. Push to GitHub
2. Connect repository to [Streamlit Cloud](https://share.streamlit.io)
3. Deploy automatically on git push

#### Option 2: Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

#### Option 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "dashboards/app.py", "--server.config", "streamlit_config.toml"]
```

### GitHub Integration
This project includes GitHub Actions for:
- **Automated Testing**: Dependencies and pipeline validation
- **Continuous Integration**: Analysis pipeline execution
- **Automated Deployment**: Dashboard deployment on main branch updates

See `.github/workflows/air_quality_health.yml` for CI/CD configuration.

## 📊 Project Structure

```
projects/air_quality_health/
├── data/                    # Raw and processed data
│   ├── openaq/             # OpenAQ PM2.5 measurements
│   └── who/                # WHO/IHME health data
├── scripts/                # Analysis scripts
│   ├── fetch_openaq.py     # Data collection
│   ├── load_health_data.py # Health data loading
│   ├── analyze_data.py     # Basic analysis
│   ├── decompose_pm25.py   # Time-series decomposition
│   ├── regress_pm25_mortality.py # Regression analysis
│   ├── forecast_pm25.py    # Prophet forecasting
│   └── make_report.py      # Report generation
├── dashboards/             # Streamlit applications
│   ├── app.py              # Basic dashboard
│   └── app_super.py        # Comprehensive dashboard
├── outputs/                # Results and visualizations
│   ├── plots/              # Charts and figures
│   ├── tables/             # Data tables and regression results
│   └── reports/            # Manuscripts and documentation
└── run_*.py                # Pipeline runners
```

## 🔬 Analysis Pipeline

### Basic Analysis (`run_all.py`)
1. **Data Collection**: Fetch PM2.5 data from OpenAQ API
2. **Health Data**: Load WHO/IHME mortality rates
3. **Analysis**: Generate city rankings and basic visualizations
4. **Reporting**: Create comprehensive manuscript

### Extended Analysis (`run_extended.py`)
1. **Time-series Decomposition**: Analyze seasonal patterns
2. **Regression Modeling**: PM2.5 vs mortality relationships

### Forecasting (`run_forecast.py`)
1. **Prophet Models**: 30-day PM2.5 predictions for each city

## 📈 Key Features

### Real-time Data Integration
- Automated fetching of current PM2.5 measurements
- Integration with global health databases
- Continuous monitoring capabilities

### Advanced Analytics
- **Time-series decomposition** with seasonal trend analysis
- **Regression modeling** with fixed effects
- **Machine learning forecasting** using Prophet
- **Interactive visualizations** with Plotly

### Comprehensive Reporting
- Automated manuscript generation
- Statistical analysis summaries
- Data quality assessments
- Reproducible research workflows

## 🌐 Dashboards

### Basic Dashboard (`app.py`)
- Current PM2.5 levels by city
- WHO/IHME health impact maps
- Real-time data visualization

### Super Dashboard (`app_super.py`)
- **Tab 1**: Current PM2.5 levels and rankings
- **Tab 2**: Time-series trends and decomposition
- **Tab 3**: 30-day forecasting with confidence intervals
- **Tab 4**: Regression results and health impact analysis

## 📋 Requirements

### Core Dependencies
- pandas, numpy, matplotlib, seaborn
- plotly, streamlit, requests
- statsmodels, prophet, geopandas
- tqdm, pypandoc

### System Requirements
- Python 3.8+
- Internet connection for API access
- 4GB+ RAM for large datasets

## 🔧 Configuration

### API Keys (Optional)
- OpenAQ API (public, no key required)
- WHO/IHME data (public datasets)

### Customization
- Modify country/region in `fetch_openaq.py`
- Adjust forecasting periods in `forecast_pm25.py`
- Customize dashboard layouts in `app_*.py`

## 📊 Sample Results

### Current Analysis (India)
- **Top Polluted Cities**: Delhi, Mumbai, Kolkata
- **Average PM2.5**: ~45 µg/m³ (national average)
- **Health Impact**: ~1.2 million premature deaths annually

### Forecasting
- 30-day predictions for 50+ cities
- Seasonal trend analysis
- Confidence intervals for uncertainty quantification

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Add tests and documentation
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 📞 Support

For issues or questions:
1. Check the troubleshooting section in the manuscript
2. Review dashboard error messages
3. Verify API connectivity and data availability

## 🔗 Related Projects

- [OpenAQ Platform](https://openaq.org)
- [WHO Global Burden of Disease](https://www.who.int/healthinfo/global_burden_disease/en/)
- [IHME Research](https://www.healthdata.org)

---

**Project Status**: Active Development
**Last Updated**: October 2025
**Geographic Focus**: India (expandable to global)
