# System Architecture - Rwanda Export Dashboard

## 📊 Complete Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    JUPYTER NOTEBOOK ANALYSIS                        │
│                    (import_export.ipynb)                            │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ Load CSV     │→ │ Data         │→ │ Opportunity  │            │
│  │ Data Files   │  │ Analysis     │  │ Scoring      │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│         ↓                 ↓                  ↓                      │
│  ┌──────────────────────────────────────────────────┐            │
│  │   Calculate:                                      │            │
│  │   • Growth rates                                  │            │
│  │   • Market concentration (HHI)                    │            │
│  │   • Strategic market tiers                        │            │
│  │   • Opportunity scores                            │            │
│  └──────────────────────────────────────────────────┘            │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│              INSIGHTS EXTRACTION LAYER                              │
│              (export_insights_extractor.py)                         │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ ExportInsightsExtractor Class:                            │   │
│  │                                                             │   │
│  │ extract_commodity_insights()        → Top opportunities    │   │
│  │ extract_opportunity_analysis()      → Opportunity matrix   │   │
│  │ extract_market_trends()             → Trend patterns       │   │
│  │ extract_strategic_markets()         → Tier 1/2/3 markets  │   │
│  │ generate_policy_recommendations()   → 4 policy actions     │   │
│  │ generate_youth_sme_opportunities()  → 5 SME sectors        │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                     │
│  Exports to:                                                        │
│  ├─► export_insights.json (Complete structured data)               │
│  ├─► export_insights_opportunities.csv                             │
│  ├─► export_insights_opportunity_matrix.csv                        │
│  ├─► export_insights_policy_recommendations.csv                    │
│  ├─► export_insights_youth_sme_opportunities.csv                   │
│  ├─► export_insights_strategic_tier1_powerhouses.csv              │
│  ├─► export_insights_strategic_tier2_emerging.csv                 │
│  └─► export_insights_strategic_tier3_untapped.csv                 │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  WEB DASHBOARD LAYER                                │
│                  (dashboard_app.py)                                 │
│                  Streamlit Framework                                │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │                    MAIN DASHBOARD                         │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  📊 EXECUTIVE SUMMARY                              │  │    │
│  │  │  • Key metrics cards                               │  │    │
│  │  │  • Market trend indicators                         │  │    │
│  │  │  • Top 3 opportunities                             │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  🎯 TOP OPPORTUNITIES                              │  │    │
│  │  │  • Interactive bar charts                          │  │    │
│  │  │  • Opportunity matrix scatter plot                 │  │    │
│  │  │  • Detailed data table                             │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  🌍 STRATEGIC MARKETS                              │  │    │
│  │  │  Tab 1: Tier 1 Powerhouses (5 markets)            │  │    │
│  │  │  Tab 2: Tier 2 Emerging (0-5 markets)             │  │    │
│  │  │  Tab 3: Tier 3 Untapped (3 markets)               │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  📜 POLICY RECOMMENDATIONS                         │  │    │
│  │  │  • 4 recommendations (2 HIGH, 2 MEDIUM priority)   │  │    │
│  │  │  • Expandable detail panels                        │  │    │
│  │  │  • Priority distribution pie chart                 │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  👥 YOUTH & SME OPPORTUNITIES                      │  │    │
│  │  │  • 5 specific business opportunities               │  │    │
│  │  │  • Investment ranges: $2K - $200K                  │  │    │
│  │  │  • Skills, revenue potential, support programs     │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  │                                                            │    │
│  │  ┌────────────────────────────────────────────────────┐  │    │
│  │  │  📈 DETAILED ANALYTICS                             │  │    │
│  │  │  • Raw data tables                                 │  │    │
│  │  │  • Download CSV buttons                            │  │    │
│  │  │  • Additional visualizations                       │  │    │
│  │  └────────────────────────────────────────────────────┘  │    │
│  └──────────────────────────────────────────────────────────┘    │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       END USERS                                     │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ Government   │  │ Policy       │  │ Youth/SME    │            │
│  │ Officials    │  │ Makers       │  │ Entrepreneurs│            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Transformation Flow

```
RAW DATA                PROCESSED DATA           INSIGHTS               VISUALIZATIONS
(CSV files)        →    (DataFrames)        →   (JSON/CSV)        →    (Interactive)

2024Q3_Export*.csv      commodities_df          top_opportunities      Bar charts
rwanda_export*.csv  →   opportunity_analysis → opportunity_matrix  →  Scatter plots
                        tier1/2/3_markets       strategic_markets      Pie charts
                        quarterly_data          policy_recommendations Tables
                                               youth_sme_opportunities  Filters
```

## 🎯 User Journey

### Government Official Journey
```
1. Opens dashboard URL
   ↓
2. Views Executive Summary
   - Sees 5 top opportunities
   - Notes 2 HIGH priority policies
   ↓
3. Explores Strategic Markets
   - UAE: 182% growth, $590M
   - Decides to focus resources here
   ↓
4. Reviews Policy Recommendations
   - Agricultural Enhancement (HIGH)
   - Downloads CSV for ministry meeting
   ↓
5. Shares dashboard with stakeholders
```

**Authors**: Orpheus Mhizha Manga & Antony Wambugu  
**Project**: NISR Hackathon 2025
