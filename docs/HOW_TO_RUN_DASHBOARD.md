# How to Run the Dashboard

## Quick Start

### Step 1: Install Streamlit (First Time Only)

```bash
cd /yourpath/NISR-HACKATHON
pip3 install streamlit plotly
```

**Or install all requirements:**
```bash
pip3 install -r requirements.txt
```

### Step 2: Launch the Dashboard

```bash
streamlit run dashboard_app.py
```

### Step 3: Access the Dashboard

The dashboard will automatically open in your browser at:
```
http://localhost:8501
```

If it doesn't open automatically, copy the URL from the terminal and paste it into your browser.

## 📊 What You'll See

### Sidebar Navigation
- **📊 Executive Summary** - Key metrics overview
- **🎯 Top Opportunities** - Export opportunities by commodity
- **🌍 Strategic Markets** - Tier 1/2/3 market analysis
- **🔮 Predictive Forecasts** - ML predictions (if forecast data available)
- **📜 Policy Recommendations** - Strategic policy advice
- **👥 Youth & SME Opportunities** - Sector opportunities
- **📈 Detailed Analytics** - In-depth data analysis

### Interactive Features
- 📊 Dynamic charts and graphs
- 🔍 Filters and search
- 📥 Download CSV data
- 📱 Responsive design

## 🔮 Adding Predictions to Dashboard

### 1. Run Forecast Cells in Notebook

Open `import_export.ipynb` and run:
- **Cell 19**: Country-Specific Demand Forecasting
- **Cell 36**: Export Insights (will now include predictions)

### 2. Restart Dashboard

```bash
# Press Ctrl+C to stop the dashboard
# Then run again:
streamlit run dashboard_app.py
```

The **🔮 Predictive Forecasts** page will now appear!

## 🛠️ Troubleshooting

### "streamlit: command not found"
**Solution**: Install streamlit first
```bash
pip3 install streamlit plotly
```

### "No module named 'pandas'"
**Solution**: Install all requirements
```bash
pip3 install -r requirements.txt
```

### "Insights file not found"
**Solution**: Run the export cell (Cell 36) in the notebook first
```bash
# In notebook, run:
# Cell 36: Export Insights
```

### Dashboard doesn't update after adding predictions
**Solution**: Clear Streamlit cache
```bash
# Press 'C' then 'Enter' in terminal where dashboard is running
# Or click "Clear cache" in the hamburger menu (☰) in the dashboard
```

### Port already in use
**Solution**: Use a different port
```bash
streamlit run dashboard_app.py --server.port 8502
```

## Full Commands Summary
```bash
# 1. Navigate to project
cd /yourpath/NISR-HACKATHON

# 2. Install dependencies (first time only)
pip3 install streamlit plotly pandas numpy

# 3. Run the dashboard
streamlit run dashboard_app.py

# 4. Open browser (automatic or manual)
# Automatic: Dashboard opens in default browser
# Manual: Go to http://localhost:8501
```
**Authors**: Orpheus Mhizha Manga & Antony Wambugu  
**Project**: NISR Hackathon 2025 - Rwanda Export Strategy Dashboard
