# 🔮 Predictive Analytics Dashboard Guide

## Overview

Your Rwanda Export Strategy Dashboard now includes **ML-powered predictive analytics** that forecast export demand for 2023-2025 across all partner countries!

## 🎯 What's New

### Predictive Forecasts Page
A dedicated page showing:
- **Top 15 forecasted markets** for 2025
- **High-confidence growth opportunities** (>70% confidence, >20% growth)
- **Emerging market opportunities** (currently small, but high growth potential)
- **Strategic tier classifications** (A/B/C priority levels)
- **Interactive visualizations** with growth matrices and confidence scores

### Machine Learning Models
- **Linear Regression**: Captures consistent growth trends
- **Polynomial Regression**: Detects non-linear patterns
- **Ensemble Averaging**: Combines both models for robust predictions

## 📊 How to Access Predictions

### Step 1: Generate Forecast Data (In Notebook)

Run the predictive modeling cells in `import_export.ipynb`:

1. **Cell 17** (after WITS data loading): Load WITS historical data
2. **Cell 19**: Run country-specific demand forecasting
3. **Cell 21**: Generate predictive analytics dashboard
4. **Cell 22**: View strategic market prioritization

### Step 2: Export Insights with Predictions

Run the export cell **(Cell 36)**:

```python
extractor, json_file, csv_files = create_insights_export(
    commodities_df=commodities_df,
    opportunity_analysis=opportunity_analysis,
    quarterly_data=total_by_quarter,
    tier1_markets=tier1_markets,
    tier2_markets=tier2_markets,
    tier3_markets=tier3_markets,
    forecast_df=forecast_df  # 🔮 Predictions included!
)
```

This will:
✅ Extract all insights including predictions  
✅ Create `export_insights.json` with forecast data  
✅ Generate CSV files: `export_insights_forecast_*.csv`

### Step 3: Launch Dashboard

```bash
streamlit run dashboard_app.py
```

### Step 4: Navigate to Predictions

In the dashboard sidebar, select:
**🔮 Predictive Forecasts**

## 📈 Dashboard Features

### Tab 1: Top Forecasts
- Bar charts comparing current (2022) vs predicted (2025) values
- Growth rate visualization with confidence scores
- Detailed forecast table with rankings
- Download CSV functionality

### Tab 2: High Growth Markets
- Scatter plot: Growth % vs 2025 Value (bubble size = confidence)
- Identifies markets with >20% growth and >70% confidence
- Prioritized list for immediate investment

### Tab 3: Emerging Opportunities
- Markets currently <$10M but predicted >50% growth
- Long-term investment opportunities
- Visual growth trajectories

### Tab 4: Strategic Tiers
- **Tier A (Priority)**: >$50M, >20% growth, >70% confidence → Immediate action
- **Tier B (Growth)**: $10-50M, >40% growth, >60% confidence → Medium-term strategy
- **Tier C (Emerging)**: <$10M, >80% growth → Long-term monitoring
- Resource allocation recommendations
- Strategic action plan by tier

## 🎯 Key Metrics Displayed

| Metric | Description |
|--------|-------------|
| **Predicted 2025 Value** | Forecasted export value in millions |
| **Growth %** | Expected growth from 2022 to 2025 |
| **CAGR** | Compound annual growth rate (2022-2025) |
| **Confidence Score** | Model prediction reliability (0-100%) |
| **Volatility** | Market stability indicator |
| **Recommendation** | AI-generated strategic advice |

## 🚀 Use Cases

### For Government Officials
- **Identify priority markets** for trade missions
- **Allocate resources** based on ROI potential
- **Track confidence scores** to assess prediction reliability

### For Export Promotion Agencies
- **Target high-growth markets** with marketing campaigns
- **Develop market entry strategies** for Tier B markets
- **Monitor emerging opportunities** for early positioning

### For Private Sector
- **Discover untapped markets** with growth potential
- **Plan expansion strategies** based on forecasts
- **Assess market risks** via volatility and confidence metrics

## 📋 Export Recommendations by Tier

### 🔴 Tier A - Immediate Actions (6 months)
- Focus 60% of resources
- Establish direct partnerships
- Increase production capacity
- Launch targeted campaigns

### 🟡 Tier B - Medium-term (6-18 months)
- Develop market entry plans
- Build local partnerships
- Conduct feasibility studies
- Participate in trade shows

### 🟢 Tier C - Long-term (18+ months)
- Monitor quarterly developments
- Initial distributor contact
- Feasibility assessments
- Prepare for future entry

## 🔧 Troubleshooting

### "No predictive forecasts available"
**Solution**: Run the forecast cells (19-22) in the notebook first, then re-run the export cell (36)

### Predictions not showing in dashboard
**Solution**: 
1. Check `export_insights.json` contains "predictions" key
2. Restart Streamlit: `Ctrl+C` then `streamlit run dashboard_app.py`
3. Clear Streamlit cache: Click menu → Clear cache

### Low confidence scores
**Interpretation**: 
- <50% confidence = Need more historical data
- 50-70% confidence = Moderate reliability
- >70% confidence = High reliability

## 📊 Sample Output

```
🎯 STRATEGIC MARKET PRIORITIZATION
======================================================================

🔴 TIER A - PRIORITY MARKETS (Immediate Focus):
   Criteria: >$50M forecast, >20% growth, >70% confidence
   Count: 8 markets

   🌟 United Arab Emirates
      • 2025 Forecast: $524.3M
      • Growth: +45.2%
      • CAGR: 13.2%
      • Confidence: 85%
      • Action: Scale existing operations, increase marketing spend
```

## 🎓 Understanding the Models

### Linear Regression (R² Score)
- Measures how well the model fits historical trends
- R² > 0.7 = Strong predictive power
- R² < 0.5 = High uncertainty

### Polynomial Regression
- Captures acceleration/deceleration patterns
- Better for markets with non-linear growth
- Degree 2 polynomial used for balance

### Ensemble Approach
- Averages both models for robustness
- Reduces individual model biases
- Provides more stable predictions

## 💡 Pro Tips

1. **Sort by confidence** to find most reliable predictions
2. **Cross-reference with strategic markets** for validation
3. **Check volatility** - high volatility = higher risk
4. **Use CAGR** for long-term planning
5. **Download CSVs** for offline analysis in Excel

## 📞 Support

For questions or issues:
- **Technical**: Check notebook execution order
- **Data**: Verify WITS data is loaded correctly
- **Dashboard**: Ensure Streamlit is up to date (`pip install -U streamlit`)

---

**Last Updated**: October 2025  
**Authors**: Orpheus Mhizha Manga & Antony Wambugu  
**Project**: NISR Hackathon 2025 - Rwanda Export Strategy
