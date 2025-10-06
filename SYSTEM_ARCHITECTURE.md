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
│  Access via: http://localhost:8501 or deployed URL                 │
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

## 📊 Feature Matrix

| Feature | Notebook | Extractor | Dashboard |
|---------|----------|-----------|-----------|
| Data Loading | ✅ | ❌ | ❌ |
| Analysis | ✅ | ❌ | ❌ |
| Opportunity Scoring | ✅ | ❌ | ❌ |
| Insight Extraction | ❌ | ✅ | ❌ |
| Policy Generation | ❌ | ✅ | ❌ |
| JSON Export | ❌ | ✅ | ❌ |
| CSV Export | ❌ | ✅ | ❌ |
| Web Interface | ❌ | ❌ | ✅ |
| Interactive Viz | ❌ | ❌ | ✅ |
| Filtering | ❌ | ❌ | ✅ |
| Download Options | ❌ | ❌ | ✅ |

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

### Youth Entrepreneur Journey
```
1. Opens dashboard URL
   ↓
2. Navigates to "Youth & SME Opportunities"
   ↓
3. Filters by "Low Investment"
   - Finds Digital Export Platforms ($5K-$30K)
   ↓
4. Reviews required skills
   - Software Development ✓ (has this)
   - Digital Marketing ✓ (can learn)
   ↓
5. Notes support programs available
   - ICT innovation grants
   - Contacts RDB for application
```

## 💾 File Size & Performance

| File | Size | Load Time |
|------|------|-----------|
| export_insights.json | ~50 KB | <0.1s |
| All CSV files | ~100 KB | <0.2s |
| Dashboard startup | - | 1-2s |
| Page navigation | - | <0.1s |
| Chart rendering | - | 0.2-0.5s |

## 🔒 Security Considerations

```
Dashboard Security Layers:

1. Local Deployment
   └─► Only accessible on same machine
   └─► No external exposure

2. Network Deployment
   └─► Accessible only within organization
   └─► Can add authentication

3. Cloud Deployment
   └─► Can use Streamlit Cloud authentication
   └─► Or implement custom auth layer
```

## 🎨 Customization Points

```
1. Colors & Branding
   └─► dashboard_app.py: st.markdown() CSS section
   
2. Policy Recommendations
   └─► export_insights_extractor.py: generate_policy_recommendations()
   
3. Opportunity Criteria
   └─► export_insights_extractor.py: _priority_level(), _assess_risk()
   
4. Dashboard Pages
   └─► dashboard_app.py: Add new show_your_page() function
   
5. Visualizations
   └─► dashboard_app.py: Modify plotly chart configurations
```

## 📈 Scalability

The system handles:
- ✅ 100+ commodities
- ✅ 150+ countries
- ✅ 5+ years of historical data
- ✅ Thousands of data points
- ✅ Multiple concurrent users
- ✅ Real-time filtering and updates

## 🚀 Deployment Matrix

| Method | Audience | Cost | Setup Time | Maintenance |
|--------|----------|------|------------|-------------|
| Local | Self | Free | 2 min | None |
| Network | Office | Free | 5 min | Low |
| Streamlit Cloud | Public | Free | 10 min | Very Low |
| Internal Server | Organization | Variable | 1 hour | Medium |
| Docker | Any | Variable | 30 min | Low |

---

**Authors**: Orpheus Mhizha Manga & Antony Wambugu  
**Project**: NISR Hackathon 2025
