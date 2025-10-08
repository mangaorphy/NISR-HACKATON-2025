# 🚀 How to Run the Dashboard

## Quick Start

### Step 1: Install Streamlit (First Time Only)

```bash
cd /Users/cococe/Desktop/NISR-HACKATHON
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

**Currently**: Basic insights available  
**To add predictions**: Follow these steps

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

## ⚡ Pro Tips

### 1. Development Mode
For auto-reload on file changes:
```bash
streamlit run dashboard_app.py --server.runOnSave true
```

### 2. Share with Others on Network
```bash
streamlit run dashboard_app.py --server.address 0.0.0.0
```
Then share: `http://YOUR_IP:8501`

### 3. Different Browser
```bash
streamlit run dashboard_app.py --browser.serverAddress localhost
```

### 4. Stop the Dashboard
Press `Ctrl + C` in the terminal

## 📋 Complete Workflow

```bash
# 1. Navigate to project
cd /Users/cococe/Desktop/NISR-HACKATHON

# 2. Install dependencies (first time only)
pip3 install streamlit plotly pandas numpy

# 3. Run the dashboard
streamlit run dashboard_app.py

# 4. Open browser (automatic or manual)
# Automatic: Dashboard opens in default browser
# Manual: Go to http://localhost:8501
```

## 🎯 Expected Output

When you run the dashboard, you should see:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

## 📸 What the Dashboard Shows

### Without Predictions (Current State)
- Executive Summary
- Top Export Opportunities
- Strategic Markets (Tier 1, 2, 3)
- Policy Recommendations
- Youth & SME Opportunities
- Detailed Analytics

### With Predictions (After Running Forecast Cells)
- **All above pages PLUS:**
- 🔮 Predictive Forecasts page with:
  - Top 15 forecasted markets for 2025
  - High-confidence growth opportunities
  - Emerging market analysis
  - Strategic tier classifications (A/B/C)

## 🔄 Update Dashboard Data

To refresh data in the dashboard:

1. **Update notebook analysis** (run analysis cells)
2. **Run export cell** (Cell 36 in notebook)
3. **Refresh dashboard** (Click "Rerun" or press 'R' in browser)

## 📞 Need Help?

### Check these files:
- `DASHBOARD_SETUP_GUIDE.md` - Detailed setup instructions
- `ADD_PREDICTIONS_TO_DASHBOARD.md` - How to add ML predictions
- `PREDICTIVE_DASHBOARD_GUIDE.md` - Predictions user guide

### Common Commands:
```bash
# Check if streamlit is installed
pip3 show streamlit

# Check Python version (need 3.7+)
python3 --version

# List all installed packages
pip3 list

# Update streamlit
pip3 install --upgrade streamlit
```

---

## 🎉 Ready to Launch!

**Run this command now:**
```bash
cd /Users/cococe/Desktop/NISR-HACKATHON && streamlit run dashboard_app.py
```

Your dashboard will be accessible at: **http://localhost:8501** 🚀

---

**Authors**: Orpheus Mhizha Manga & Antony Wambugu  
**Project**: NISR Hackathon 2025 - Rwanda Export Strategy Dashboard
