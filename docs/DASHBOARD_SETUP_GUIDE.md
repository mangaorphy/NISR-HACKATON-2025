# Rwanda Export Strategy Dashboard - Setup Guide

## 🎯 Overview

This solution automatically extracts insights from your Jupyter Notebook analysis and creates an interactive dashboard for government experts. The system includes:

1. **Insights Extractor** - Automatically extracts key findings from your analysis
2. **Interactive Dashboard** - Beautiful web interface for government experts
3. **Automated Pipeline** - One-click export from notebook to dashboard

---

## 📋 Prerequisites

Install required packages:

```bash
pip install streamlit plotly pandas numpy
```

---

## 🚀 Quick Start Guide

### Step 1: Run Your Analysis (Jupyter Notebook)

1. Open `import_export.ipynb`
2. Run all cells in order
3. When you reach the **"Export Insights to Dashboard Pipeline"** section, run that cell
4. This will automatically generate:
   - `export_insights.json` - Complete insights in JSON format
   - Multiple CSV files - Individual data tables for each insight category

### Step 2: Launch the Dashboard

Open a terminal and run:

```bash
streamlit run dashboard_app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

### Step 3: Share with Government Experts

The dashboard includes 6 main sections:

1. **📊 Executive Summary** - High-level overview and key metrics
2. **🎯 Top Opportunities** - Detailed commodity opportunities with visualizations
3. **🌍 Strategic Markets** - Country-by-country market analysis (Tier 1, 2, 3)
4. **📜 Policy Recommendations** - Actionable policy suggestions with priority levels
5. **👥 Youth & SME Opportunities** - Specific opportunities for entrepreneurs
6. **📈 Detailed Analytics** - Deep-dive data tables and charts

---

## 📊 What Gets Automatically Extracted

### 1. Top Export Opportunities

- Top commodities by value and growth
- Opportunity scores (0-100)
- Risk assessments
- Action priorities

### 2. Strategic Market Analysis

- **Tier 1 Powerhouses**: High-growth, high-value markets (e.g., UAE, Ethiopia, India)
- **Tier 2 Emerging**: Fast-growing medium markets
- **Tier 3 Untapped**: New markets with potential

### 3. Policy Recommendations

Generated automatically based on your data:

- Agricultural export enhancement (Q3 seasonal opportunities)
- Market diversification (reduce concentration risk)
- Value chain development (processing infrastructure)
- Strategic market entry (focus countries)

Each recommendation includes:

- Priority level (HIGH/MEDIUM/LOW)
- Target stakeholders
- Timeline
- Expected impact

### 4. Youth & SME Opportunities

Specific actionable opportunities:

- **Agribusiness Aggregation** - Low investment ($5K-$50K)
- **Cold Chain & Logistics** - Medium-high investment ($50K-$200K)
- **Value-Added Processing** - Medium investment ($20K-$100K)
- **Digital Export Platforms** - Low investment ($5K-$30K)
- **Export Documentation Services** - Very low investment ($2K-$10K)

Each opportunity includes:

- Investment required
- Skills needed
- Revenue potential
- Market demand
- Available support programs

---

## 🔄 The Automated Pipeline

```
┌─────────────────────────────┐
│  Jupyter Notebook Analysis  │
│  (import_export.ipynb)      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Insights Extractor         │
│  (export_insights_         │
│   extractor.py)             │
└──────────────┬──────────────┘
               │
               ├──► export_insights.json
               ├──► export_insights_opportunities.csv
               ├──► export_insights_opportunity_matrix.csv
               ├──► export_insights_policy_recommendations.csv
               ├──► export_insights_youth_sme_opportunities.csv
               ├──► export_insights_strategic_tier1_powerhouses.csv
               ├──► export_insights_strategic_tier2_emerging.csv
               └──► export_insights_strategic_tier3_untapped.csv
               │
               ▼
┌─────────────────────────────┐
│  Interactive Dashboard      │
│  (dashboard_app.py)         │
│  → Streamlit Web App        │
└─────────────────────────────┘
```

---

## 💡 Key Features

### For Data Scientists

- **One-click export**: Run one cell, get all insights exported
- **Multiple formats**: JSON for web apps, CSV for Excel/analysis
- **Structured data**: Clean, well-organized output

### For Government Experts

- **Interactive visualizations**: Plotly charts with hover details
- **Filtering capabilities**: Priority filters, sector filters
- **Download options**: Export data to CSV for reports
- **Mobile responsive**: Works on tablets and phones

### For Policy Makers

- **Priority-based recommendations**: Focus on HIGH priority items first
- **Clear action items**: Specific stakeholders, timelines, expected impacts
- **Evidence-based**: All recommendations derived from data analysis

---

## 🎨 Dashboard Features

### Executive Summary

- Key performance metrics
- Market trend indicators
- Top 3 opportunities at a glance
- Quick decision-making insights

### Visualizations Include

- Bar charts for rankings
- Scatter plots for opportunity matrices
- Pie charts for distributions
- Growth trend lines
- Interactive hover tooltips
- Color-coded risk levels

### Export Capabilities

- Download any data table as CSV
- Share specific insights
- Generate reports

---

## 🔧 Customization

### Modify Policy Recommendations

Edit `export_insights_extractor.py`, function `generate_policy_recommendations()`:

```python
def generate_policy_recommendations(self):
    self.insights['policy_recommendations'] = [
        {
            'priority': 'HIGH',
            'area': 'Your Custom Area',
            'recommendation': 'Your recommendation text',
            # ... add more fields
        }
    ]
```

### Add New Dashboard Pages

Edit `dashboard_app.py`, add new function:

```python
def show_your_new_page(insights):
    st.header("Your New Page")
    # Add your content
```

### Change Dashboard Styling

Modify the CSS in `dashboard_app.py`:

```python
st.markdown("""
    <style>
    /* Your custom CSS */
    </style>
""", unsafe_allow_html=True)
```

---

## 📱 Deployment Options

### Option 1: Local Network (For Government Office)

```bash
streamlit run dashboard_app.py --server.port 8501
```

Share: `http://YOUR_IP_ADDRESS:8501`

### Option 2: Streamlit Cloud (Free Hosting)

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your repository
4. Deploy!

### Option 3: Internal Server

Deploy on your organization's server using Docker:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "dashboard_app.py"]
```

---

## 📞 Support & Troubleshooting

### Common Issues

**1. "Insights file not found"**

- Solution: Run the notebook cell that exports insights first

**2. "Module not found: streamlit"**

- Solution: `pip install streamlit plotly`

**3. "Port already in use"**

- Solution: `streamlit run dashboard_app.py --server.port 8502`

**4. Empty data in dashboard**

- Solution: Ensure all notebook cells ran successfully before exporting

---

## 🎯 Success Metrics

The dashboard helps track:

- ✅ Number of high-priority opportunities identified
- ✅ Strategic markets for expansion
- ✅ Youth/SME engagement potential
- ✅ Policy implementation timelines
- ✅ Expected economic impact

---

## 👥 Authors

**Orpheus Mhizha Manga** & **Antony Wambugu**

NISR Hackathon 2025 - Rwanda Export Opportunity Analysis

---

## 📄 License

This project is created for the NISR Hackathon 2025 and is intended for government and educational use.

---

## 🌟 Next Steps

1. ✅ Run the notebook analysis
2. ✅ Export insights automatically
3. ✅ Launch the dashboard
4. 🎯 Share with government experts
5. 📊 Use insights for policy decisions
6. 🚀 Implement recommendations
7. 📈 Track export growth!

---

**Questions?** Check the inline documentation in:

- `export_insights_extractor.py` - Extraction logic
- `dashboard_app.py` - Dashboard components
- `import_export.ipynb` - Analysis workflow
