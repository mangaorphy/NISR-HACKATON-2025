# Data Directory Structure

## Overview
This directory contains all data files used in the Rwanda Export Strategy Dashboard project.

## Directory Structure

```
data/
├── raw/              # Original Q3 2024 export data from NISR
├── wits/             # Historical WITS data (2018-2022)
├── processed/        # Cleaned and analysis-ready datasets
└── insights/         # Generated insights and predictions
```

## 📁 Folders Explained

### `/raw` - Raw Data Files
Original Q3 2024 export data directly from NISR reports:
- `2024Q3_ExportCountry.csv` - Export by destination country
- `2024Q3_ExportsCommodity.csv` - Export by commodity (SITC codes)
- `2024Q3_ReexportsCommodity.csv` - Re-export data
- `2024Q3_Regional blocks.csv` - Regional trade blocks analysis
- `2024Q3_Trade by continents.csv` - Continental trade distribution
- `2024Q3_Trade_report_annexTables_0.xlsx - Total trade with the World.csv` - Total trade summary

**Purpose**: Keep original data untouched for reproducibility

### `/wits` - WITS Historical Data
World Bank WITS (World Integrated Trade Solution) data for Rwanda (2018-2022):
- `rwanda_export_partners_2018_2022_combined.csv` - Partner country trade over 5 years
- `rwanda_exports_growth_analysis_2018_2022.csv` - Growth rate analysis
- `rwanda_exports_regional_analysis_2018_2022.csv` - Regional patterns
- `rwanda_exports_yearly_summary_2018_2022.csv` - Year-by-year summaries

**Purpose**: Historical data for predictive modeling and trend analysis

### `/processed` - Processed Data
Cleaned and prepared datasets ready for analysis:
- `analysis_ready_total_trade_world_updated.csv` - Merged and cleaned total trade data

**Purpose**: Analysis-ready data with consistent formatting

### `/insights` - Generated Insights
Automatically generated insights from the analysis:
- `export_insights.json` - Complete insights package for dashboard
- `export_insights_opportunities.csv` - Top export opportunities
- `export_insights_opportunity_matrix.csv` - Opportunity scoring matrix
- `export_insights_policy_recommendations.csv` - Strategic policy recommendations
- `export_insights_strategic_tier1_powerhouses.csv` - Tier 1 priority markets
- `export_insights_strategic_tier2_emerging.csv` - Tier 2 growth markets
- `export_insights_strategic_tier3_untapped.csv` - Tier 3 emerging markets
- `export_insights_youth_sme_opportunities.csv` - Youth and SME sector opportunities
- `export_insights_forecast_*.csv` - Predictive forecasts (when generated)

**Purpose**: Dashboard data feeds and exportable insights

## 🔄 Data Flow

```
Raw Data → Processing → Analysis → Insights → Dashboard
   ↓           ↓           ↓          ↓           ↓
 /raw/    /processed/   Notebook  /insights/  Streamlit
```

## 📝 File Naming Conventions

- **Raw files**: `YYYYQN_Description.csv` (e.g., 2024Q3_ExportCountry.csv)
- **WITS files**: `rwanda_exports_description_YYYY_YYYY.csv`
- **Insights files**: `export_insights_category.csv`
- **Processed files**: `description_analysis_ready.csv`

## 📊 Data Sources

1. **NISR (National Institute of Statistics Rwanda)** - Q3 2024 data
2. **WITS (World Bank)** - Historical data 2018-2022
3. **Generated** - Insights from ML models and analysis

## Usage

To use these files in the notebook or dashboard:
```python
# Raw data
raw_data = pd.read_csv('data/raw/2024Q3_ExportCountry.csv')

# WITS data
wits_data = pd.read_csv('data/wits/rwanda_export_partners_2018_2022_combined.csv')

# Insights
insights = json.load(open('data/insights/export_insights.json'))
```

## 🔄 Updating Data

When new data arrives:
1. Place raw files in `/raw/`
2. Run processing notebook cells
3. Save processed files to `/processed/`
4. Generate new insights to `/insights/`

---

**Last Updated**: October 2025  
**Project**: NISR Hackathon 2025 - Rwanda Export Strategy
