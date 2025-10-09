"""
Rwanda Export Strategy Dashboard
Interactive dashboard for government experts
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Rwanda Export Strategy Dashboard",
    page_icon="🇷🇼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3B82F6;
    }
    .priority-high {
        color: #DC2626;
        font-weight: bold;
    }
    .priority-medium {
        color: #F59E0B;
        font-weight: bold;
    }
    .priority-low {
        color: #10B981;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_insights():
    """Load insights from JSON file"""
    try:
        with open('data/insights/export_insights.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("❌ Insights file not found. Please run the analysis notebook first.")
        return None

@st.cache_data
def load_csv_data(filename):
    """Load CSV data files"""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None

# Main dashboard
def main():
    # Header
    st.markdown('<h1 class="main-header">🇷🇼 Rwanda Export Strategy Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Data-Driven Insights for Export Growth & Policy Development")
    
    # Load insights
    insights = load_insights()
    
    if insights is None:
        st.warning("⚠️ Please generate insights by running the analysis notebook first.")
        st.stop()
    
    # Sidebar navigation
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/320px-Flag_of_Rwanda.svg.png", width=200)
    st.sidebar.title("Navigation")
    
    # Check if predictions are available
    has_predictions = 'predictions' in insights and insights['predictions']
    
    pages = ["📊 Executive Summary", "🎯 Top Opportunities", "🌍 Strategic Markets", 
             "📜 Policy Recommendations", "👥 Youth & SME Opportunities", "📈 Detailed Analytics"]
    
    if has_predictions:
        pages.insert(3, "🔮 Predictive Forecasts")  # Add predictions page
    
    page = st.sidebar.radio("Select View", pages)
    
    # Display metadata
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Report Period:** {insights['metadata']['report_period']}")
    st.sidebar.markdown(f"**Generated:** {insights['metadata']['generated_at'][:10]}")
    
    if has_predictions:
        st.sidebar.success("🔮 Predictions Available!")
    
    # Page routing
    if page == "📊 Executive Summary":
        show_executive_summary(insights)
    elif page == "🎯 Top Opportunities":
        show_top_opportunities(insights)
    elif page == "🌍 Strategic Markets":
        show_strategic_markets(insights)
    elif page == "🔮 Predictive Forecasts":
        show_predictive_forecasts(insights)
    elif page == "📜 Policy Recommendations":
        show_policy_recommendations(insights)
    elif page == "👥 Youth & SME Opportunities":
        show_youth_sme_opportunities(insights)
    elif page == "📈 Detailed Analytics":
        show_detailed_analytics(insights)


def show_executive_summary(insights):
    """Executive summary page"""
    st.header("📊 Executive Summary")
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        top_opps = len(insights.get('top_opportunities', []))
        st.metric("Top Opportunities", top_opps, "identified")
    
    with col2:
        high_priority = len([p for p in insights.get('policy_recommendations', []) if p['priority'] == 'HIGH'])
        st.metric("High Priority Policies", high_priority, "recommendations")
    
    with col3:
        youth_sectors = len(insights.get('youth_sme_opportunities', []))
        st.metric("Youth/SME Sectors", youth_sectors, "opportunities")
    
    with col4:
        if 'strategic_markets' in insights:
            tier1_count = len(insights['strategic_markets'].get('tier1_powerhouses', []))
            st.metric("Tier 1 Markets", tier1_count, "powerhouses")
    
    st.markdown("---")
    
    # Market trends
    if 'market_trends' in insights:
        st.subheader("📈 Market Trends Overview")
        trends = insights['market_trends']
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Overall Trend:** {trends.get('total_exports_trend', 'N/A').upper()}")
            st.info(f"**Average Growth Rate:** {trends.get('growth_rate_avg', 0):.1f}%")
        
        with col2:
            seasonal = trends.get('seasonal_patterns', {})
            st.info(f"**Peak Quarter:** {seasonal.get('peak_quarter', 'N/A')}")
            st.info(f"**Volatility Index:** {trends.get('volatility_index', 'N/A')}")
    
    # Top 3 opportunities highlight
    st.markdown("---")
    st.subheader("🏆 Top 3 Export Opportunities")
    
    if 'opportunity_matrix' in insights:
        top_3 = insights['opportunity_matrix'][:3]
        
        for idx, opp in enumerate(top_3, 1):
            with st.expander(f"#{idx} {opp['commodity']} (Score: {opp['opportunity_score']:.1f}/100)", expanded=idx==1):
                cols = st.columns(4)
                cols[0].metric("Growth Rate", f"{opp['growth_rate']:.1f}%")
                cols[1].metric("Market Share", f"{opp['market_share']:.1f}%")
                cols[2].metric("Risk Level", opp['risk_level'])
                cols[3].metric("Priority", opp['action_priority'])


def show_top_opportunities(insights):
    """Top opportunities detailed view"""
    st.header("🎯 Top Export Opportunities")
    
    # Load opportunity matrix data
    opp_df = load_csv_data('data/insights/export_insights_opportunity_matrix.csv')
    
    if opp_df is not None:
        # Opportunity score chart
        fig = px.bar(
            opp_df.head(10),
            x='opportunity_score',
            y='commodity',
            orientation='h',
            title="Top 10 Opportunities by Score",
            labels={'opportunity_score': 'Opportunity Score', 'commodity': 'Commodity'},
            color='opportunity_score',
            color_continuous_scale='Viridis'
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # Opportunity matrix scatter
        st.subheader("📊 Opportunity Matrix: Growth vs Market Share")
        fig2 = px.scatter(
            opp_df,
            x='market_share',
            y='growth_rate',
            size='opportunity_score',
            color='risk_level',
            hover_data=['commodity'],
            title="Growth Rate vs Market Share (Bubble size = Opportunity Score)",
            labels={'market_share': 'Market Share (%)', 'growth_rate': 'Growth Rate (%)'},
            color_discrete_map={'LOW': 'green', 'MEDIUM': 'orange', 'HIGH': 'red'}
        )
        fig2.update_layout(height=500)
        st.plotly_chart(fig2, use_container_width=True)
        
        # Detailed table
        st.subheader("📋 Detailed Opportunity Analysis")
        display_df = opp_df[['commodity', 'opportunity_score', 'growth_rate', 'market_share', 'risk_level', 'action_priority']]
        display_df.columns = ['Commodity', 'Score', 'Growth %', 'Market Share %', 'Risk', 'Priority']
        st.dataframe(display_df, use_container_width=True)


def show_strategic_markets(insights):
    """Strategic markets page"""
    st.header("🌍 Strategic Market Opportunities")
    
    if 'strategic_markets' not in insights:
        st.warning("Strategic markets data not available")
        return
    
    markets = insights['strategic_markets']
    
    # Tier tabs
    tab1, tab2, tab3 = st.tabs(["🏆 Tier 1: Powerhouses", "Tier 2: Emerging", " Tier 3: Untapped"])
    
    with tab1:
        st.subheader("High Growth Powerhouse Markets")
        st.markdown("**Strategy:** Scale & Deepen market presence")
        
        tier1 = markets.get('tier1_powerhouses', [])
        if tier1:
            df = pd.DataFrame(tier1)
            
            # Visualization
            fig = px.bar(
                df,
                x='growth_rate',
                y='country',
                orientation='h',
                color='value_2022_millions',
                title="Tier 1 Markets: Growth Rate & Value",
                labels={'growth_rate': 'Growth Rate (%)', 'country': 'Country', 'value_2022_millions': '2022 Value ($M)'}
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Table
            st.dataframe(df, use_container_width=True)
    
    with tab2:
        st.subheader("Emerging Market Opportunities")
        st.markdown("**Strategy:** Rapid Expansion")
        
        tier2 = markets.get('tier2_emerging', [])
        if tier2:
            df = pd.DataFrame(tier2)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No Tier 2 markets identified in current analysis")
    
    with tab3:
        st.subheader("Untapped Potential Markets")
        st.markdown("**Strategy:** Market Entry & Development")
        
        tier3 = markets.get('tier3_untapped', [])
        if tier3:
            df = pd.DataFrame(tier3)
            
            fig = px.bar(
                df,
                x='growth_rate',
                y='country',
                orientation='h',
                title="Tier 3 Markets: Growth Potential",
                labels={'growth_rate': 'Growth Rate (%)', 'country': 'Country'}
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.dataframe(df, use_container_width=True)


def show_predictive_forecasts(insights):
    """Predictive analytics and forecasts page"""
    st.header("🔮 Predictive Forecasts: 2023-2025")
    st.markdown("### ML-Powered Export Demand Predictions")
    
    predictions = insights.get('predictions', {})
    
    if not predictions:
        st.warning("⚠️ No Predictive Forecasts available. Run the predictive model in the notebook first.")
        return
    
    # Summary metrics
    summary = predictions.get('summary', {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Countries Forecasted",
            summary.get('total_countries', 0),
            help="Number of partner countries with predictions"
        )
    
    with col2:
        predicted_2025 = summary.get('total_predicted_2025', 0)
        st.metric(
            "Predicted 2025 Exports",
            f"${predicted_2025:.1f}M",
            help="Total forecasted export value for 2025"
        )
    
    with col3:
        growth = summary.get('overall_growth_percent', 0)
        st.metric(
            "Overall Growth vs 2022",
            f"{growth:+.1f}%",
            delta=f"{growth:.1f}%",
            help="Expected growth from 2022 to 2025"
        )
    
    with col4:
        confidence = summary.get('avg_confidence', 0)
        st.metric(
            "Avg Model Confidence",
            f"{confidence:.1f}%",
            help="Average prediction confidence across all countries"
        )
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Top Forecasts", 
        "High Growth Markets", 
        "Emerging Opportunities",
        "Strategic Tiers"
    ])
    
    with tab1:
        st.subheader("Top 15 Forecasted Markets for 2025")
        
        top_forecasts = predictions.get('top_forecasts', [])
        
        if top_forecasts:
            # Create visualization
            df = pd.DataFrame(top_forecasts)
            
            # Bar chart: Current vs Predicted
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                name='Current 2022',
                x=df['country'],
                y=df['current_2022_millions'],
                marker_color='lightblue'
            ))
            
            fig.add_trace(go.Bar(
                name='Predicted 2025',
                x=df['country'],
                y=df['predicted_2025_millions'],
                marker_color='darkblue'
            ))
            
            fig.update_layout(
                title="Current (2022) vs Predicted (2025) Export Values",
                xaxis_title="Country",
                yaxis_title="Export Value ($ Millions)",
                barmode='group',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Growth rate visualization
            fig2 = px.bar(
                df,
                x='growth_percent',
                y='country',
                orientation='h',
                color='confidence_score',
                color_continuous_scale='RdYlGn',
                title="Predicted Growth Rate by Country (2022-2025)",
                labels={
                    'growth_percent': 'Growth %',
                    'country': 'Country',
                    'confidence_score': 'Confidence'
                }
            )
            fig2.update_layout(height=600)
            st.plotly_chart(fig2, use_container_width=True)
            
            # Detailed table
            st.subheader("📋 Detailed Forecast Data")
            
            display_df = df[[
                'rank', 'country', 'current_2022_millions', 'predicted_2025_millions',
                'growth_percent', 'cagr_2022_2025', 'confidence_score', 'recommendation'
            ]].copy()
            
            display_df.columns = [
                'Rank', 'Country', 'Current 2022 ($M)', 'Predicted 2025 ($M)',
                'Growth %', 'CAGR %', 'Confidence %', 'Recommendation'
            ]
            
            st.dataframe(
                display_df.style.background_gradient(subset=['Growth %'], cmap='RdYlGn')
                         .background_gradient(subset=['Confidence %'], cmap='Blues'),
                use_container_width=True
            )
            
            # Download button
            csv = display_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Top Forecasts CSV",
                data=csv,
                file_name="rwanda_export_forecasts_top15.csv",
                mime="text/csv"
            )
        else:
            st.info("No forecast data available")
    
    with tab2:
        st.subheader("🚀 High-Confidence Growth Markets")
        st.markdown("**Criteria:** >20% growth, >70% confidence")
        
        high_growth = predictions.get('high_growth_markets', [])
        
        if high_growth:
            df = pd.DataFrame(high_growth)
            
            # Scatter plot
            fig = px.scatter(
                df,
                x='growth_percent',
                y='predicted_2025_millions',
                size='confidence_score',
                color='growth_percent',
                hover_name='country',
                color_continuous_scale='Viridis',
                title="Growth vs Value Matrix (bubble size = confidence)",
                labels={
                    'growth_percent': 'Predicted Growth %',
                    'predicted_2025_millions': 'Predicted 2025 Value ($M)',
                    'confidence_score': 'Confidence'
                }
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Table
            display_df = df.copy()
            display_df.columns = ['Country', 'Predicted 2025 ($M)', 'Growth %', 'Confidence %']
            
            st.dataframe(
                display_df.style.background_gradient(subset=['Growth %'], cmap='Greens'),
                use_container_width=True
            )
            
            st.success(f"✅ **{len(high_growth)} high-confidence growth markets identified**")
            st.markdown("**Action:** Prioritize these markets for immediate investment and partnership development")
        else:
            st.info("No high-confidence growth markets identified")
    
    with tab3:
        st.subheader(" Emerging Market Opportunities")
        st.markdown("**Criteria:** Currently <$10M, but >50% predicted growth")
        
        emerging = predictions.get('emerging_opportunities', [])
        
        if emerging:
            df = pd.DataFrame(emerging)
            
            # Visualization
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=df['current_2022_millions'],
                y=df['predicted_2025_millions'],
                mode='markers+text',
                marker=dict(
                    size=df['growth_percent']/5,
                    color=df['growth_percent'],
                    colorscale='Plasma',
                    showscale=True,
                    colorbar=dict(title="Growth %")
                ),
                text=df['country'],
                textposition="top center",
                hovertemplate='<b>%{text}</b><br>Current: $%{x:.1f}M<br>Predicted: $%{y:.1f}M<extra></extra>'
            ))
            
            fig.update_layout(
                title="Emerging Markets: Current vs Predicted Values",
                xaxis_title="Current 2022 ($M)",
                yaxis_title="Predicted 2025 ($M)",
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Table
            display_df = df.copy()
            display_df.columns = ['Country', 'Current 2022 ($M)', 'Predicted 2025 ($M)', 'Growth %']
            
            st.dataframe(
                display_df.style.background_gradient(subset=['Growth %'], cmap='Oranges'),
                use_container_width=True
            )
            
            st.info(f"💡 **{len(emerging)} emerging markets** - Long-term investment opportunities")
        else:
            st.info("No emerging markets identified")
    
    with tab4:
        st.subheader("🎯 Strategic Market Tiers (ML Classification)")
        
        tiers = predictions.get('tier_classifications', {})
        
        if tiers:
            # Tier summary
            col1, col2, col3 = st.columns(3)
            
            with col1:
                tier_a = tiers.get('tier_a_priority', {})
                st.markdown("### 🔴 Tier A - Priority")
                st.metric("Markets", tier_a.get('count', 0))
                st.metric("2025 Value", f"${tier_a.get('total_value_2025', 0):.1f}M")
                st.caption(">$50M forecast, >20% growth, >70% confidence")
                
                if tier_a.get('countries'):
                    with st.expander("View Countries"):
                        for country in tier_a['countries']:
                            st.write(f"• {country}")
            
            with col2:
                tier_b = tiers.get('tier_b_growth', {})
                st.markdown("### 🟡 Tier B - Growth")
                st.metric("Markets", tier_b.get('count', 0))
                st.metric("2025 Value", f"${tier_b.get('total_value_2025', 0):.1f}M")
                st.caption("$10-50M forecast, >40% growth, >60% confidence")
                
                if tier_b.get('countries'):
                    with st.expander("View Countries"):
                        for country in tier_b['countries']:
                            st.write(f"• {country}")
            
            with col3:
                tier_c = tiers.get('tier_c_emerging', {})
                st.markdown("### 🟢 Tier C - Emerging")
                st.metric("Markets", tier_c.get('count', 0))
                st.metric("2025 Value", f"${tier_c.get('total_value_2025', 0):.1f}M")
                st.caption("<$10M forecast, >80% growth, >0.5M current")
                
                if tier_c.get('countries'):
                    with st.expander("View Countries"):
                        for country in tier_c['countries']:
                            st.write(f"• {country}")
            
            st.markdown("---")
            
            # Resource allocation pie chart
            total_value = (
                tier_a.get('total_value_2025', 0) + 
                tier_b.get('total_value_2025', 0) + 
                tier_c.get('total_value_2025', 0)
            )
            
            if total_value > 0:
                fig = go.Figure(data=[go.Pie(
                    labels=['Tier A - Priority', 'Tier B - Growth', 'Tier C - Emerging'],
                    values=[
                        tier_a.get('total_value_2025', 0),
                        tier_b.get('total_value_2025', 0),
                        tier_c.get('total_value_2025', 0)
                    ],
                    marker_colors=['#DC2626', '#F59E0B', '#10B981'],
                    hole=0.4
                )])
                
                fig.update_layout(
                    title="Recommended Resource Allocation by Tier (2025 Value)",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            # Strategic recommendations
            st.subheader("📋 Strategic Action Plan")
            
            st.markdown("""
            **🔴 Tier A - Immediate Actions (Next 6 months):**
            - Focus 60% of export resources on these markets
            - Establish direct partnerships and distribution networks
            - Increase inventory and production capacity
            - Launch targeted marketing campaigns
            
            **🟡 Tier B - Medium-term Strategy (6-18 months):**
            - Develop comprehensive market entry strategies
            - Build local partnerships and presence
            - Invest in market research and feasibility studies
            - Participate in trade missions and exhibitions
            
            **🟢 Tier C - Long-term Investment (18+ months):**
            - Monitor market developments quarterly
            - Establish initial contact with distributors
            - Conduct detailed feasibility assessments
            - Prepare for future market entry when conditions improve
            """)
        else:
            st.info("No tier classifications available")


def show_policy_recommendations(insights):
    """Policy recommendations page"""
    st.header("📜 Policy Recommendations")
    
    policies = insights.get('policy_recommendations', [])
    
    if not policies:
        st.warning("No policy recommendations available")
        return
    
    # Filter by priority
    priority_filter = st.selectbox("Filter by Priority", ["All", "HIGH", "MEDIUM", "LOW"])
    
    filtered_policies = policies if priority_filter == "All" else [p for p in policies if p['priority'] == priority_filter]
    
    # Display policies
    for idx, policy in enumerate(filtered_policies, 1):
        priority_class = f"priority-{policy['priority'].lower()}"
        
        # Get the title - support both old and new format
        policy_title = policy.get('policy_title', policy.get('category', policy.get('area', 'Policy')))
        
        # Priority emoji
        priority_emoji = '🔴' if policy['priority'] in ['CRITICAL', 'HIGH'] else '🟡' if policy['priority']=='MEDIUM' else '🟢'
        
        with st.expander(f"{priority_emoji} [{policy['priority']}] {policy_title}", expanded=policy['priority'] in ['CRITICAL', 'HIGH']):
            # Category and Priority Badge
            col_badge1, col_badge2 = st.columns([3, 1])
            with col_badge1:
                st.markdown(f"**Category:** {policy.get('category', policy.get('area', 'N/A'))}")
            with col_badge2:
                st.markdown(f"<span class='{priority_class}' style='padding: 4px 12px; border-radius: 4px;'>{policy['priority']}</span>", unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Main recommendation
            st.markdown("### 📋 Policy Recommendation")
            st.markdown(policy['recommendation'])
            
            # Rationale and evidence
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**📊 Rationale:**")
                st.info(policy['rationale'])
            with col2:
                if 'data_evidence' in policy:
                    st.markdown("**📈 Data Evidence:**")
                    st.success(policy['data_evidence'])
            
            # Implementation section
            if 'implementation_actions' in policy:
                st.markdown("### 🎯 Implementation Actions")
                for action in policy['implementation_actions']:
                    st.markdown(f"  - {action}")
            
            # Stakeholders
            st.markdown("### 🤝 Key Stakeholders")
            stakeholder_cols = st.columns(min(len(policy['target_stakeholders']), 3))
            for idx_s, stakeholder in enumerate(policy['target_stakeholders']):
                with stakeholder_cols[idx_s % len(stakeholder_cols)]:
                    st.markdown(f"• {stakeholder}")
            
            # Budget and Timeline
            col_budget, col_timeline = st.columns(2)
            with col_budget:
                if 'budget_estimate' in policy:
                    st.markdown(f"**💰 Budget:** {policy['budget_estimate']}")
                else:
                    st.markdown(f"**Timeline:** {policy['timeline']}")
            with col_timeline:
                st.markdown(f"**⏱️ Implementation:** {policy.get('timeline', 'N/A')}")
            
            # Expected Impact
            st.markdown("### 🚀 Expected Impact")
            st.markdown(f"**{policy['expected_impact']}**")
            
            # Success Metrics
            if 'success_metrics' in policy:
                st.markdown("### 📊 Success Metrics")
                metric_cols = st.columns(min(len(policy['success_metrics']), 2))
                for idx_m, metric in enumerate(policy['success_metrics']):
                    with metric_cols[idx_m % len(metric_cols)]:
                        st.markdown(f"✓ {metric}")
            
            # Risks and Mitigation
            if 'risks' in policy and 'mitigation' in policy:
                st.markdown("---")
                col_risk, col_mit = st.columns(2)
                with col_risk:
                    st.markdown("**⚠️ Risks:**")
                    st.warning(policy['risks'])
                with col_mit:
                    st.markdown("**🛡️ Mitigation:**")
                    st.success(policy['mitigation'])
    
    # Summary visualization
    st.markdown("---")
    st.subheader("📊 Policy Priority Distribution")
    
    priority_counts = pd.DataFrame(policies)['priority'].value_counts()
    fig = px.pie(
        values=priority_counts.values,
        names=priority_counts.index,
        title="Policy Recommendations by Priority",
        color_discrete_map={'CRITICAL': '#B91C1C', 'HIGH': '#DC2626', 'MEDIUM': '#F59E0B', 'LOW': '#10B981'}
    )
    st.plotly_chart(fig, width="stretch")
    
    

def show_youth_sme_opportunities(insights):
    """Youth and SME opportunities page"""
    st.header("👥 Youth & SME Opportunities")
    
    opportunities = insights.get('youth_sme_opportunities', [])
    
    if not opportunities:
        st.warning("No youth/SME opportunities available")
        return
    
    st.markdown("""
    These opportunities are specifically designed for **youth entrepreneurs** and **small-to-medium enterprises (SMEs)** 
    looking to enter Rwanda's export value chain.
    """)
    
    # Sector filter
    sectors = list(set([opp['sector'] for opp in opportunities]))
    selected_sector = st.selectbox("Filter by Sector", ["All"] + sectors)
    
    filtered_opps = opportunities if selected_sector == "All" else [o for o in opportunities if o['sector'] == selected_sector]
    
    # Display opportunities as cards
    for opp in filtered_opps:
        with st.expander(f"💼 {opp['sector']}: {opp['opportunity']}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**💰 Investment Required:** {opp['investment_required']}")
                st.markdown(f"**📚 Skills Needed:**")
                for skill in opp['skills_needed']:
                    st.markdown(f"  - {skill}")
                st.markdown(f"**💵 Revenue Potential:** {opp['potential_revenue']}")
            
            with col2:
                st.markdown(f"**📊 Market Demand:** {opp['market_demand']}")
                st.markdown(f"**🤝 Support Available:** {opp['support_available']}")
    
    # Investment matrix
    st.markdown("---")
    st.subheader("📊 Investment vs Revenue Potential Matrix")
    
    df = pd.DataFrame(opportunities)
    
    # Create investment level mapping
    investment_map = {
        'Very Low ($2K-$10K)': 1,
        'Low ($5K-$30K)': 2,
        'Low-Medium ($5K-$50K)': 3,
        'Medium ($20K-$100K)': 4,
        'Medium-High ($50K-$200K)': 5
    }
    
    df['investment_score'] = df['investment_required'].map(investment_map)
    
    fig = px.scatter(
        df,
        x='investment_score',
        y='sector',
        size=[5]*len(df),
        color='potential_revenue',
        title="Youth & SME Opportunities: Investment Level by Sector",
        labels={'investment_score': 'Investment Level', 'sector': 'Sector'},
        hover_data=['opportunity']
    )
    st.plotly_chart(fig, use_container_width=True)


def show_detailed_analytics(insights):
    """Detailed analytics page"""
    st.header("📈 Detailed Analytics")
    
    # Load all CSV files
    opportunities_df = load_csv_data('data/insights/export_insights_opportunities.csv')
    matrix_df = load_csv_data('data/insights/export_insights_opportunity_matrix.csv')
    
    if opportunities_df is not None:
        st.subheader("📦 Current Export Commodities")
        
        # Value distribution
        fig = px.pie(
            opportunities_df,
            values='current_value_millions',
            names='commodity',
            title="Export Value Distribution (Top Commodities)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Growth vs Value scatter
        st.subheader("📊 Growth vs Current Value Analysis")
        fig2 = px.scatter(
            opportunities_df,
            x='current_value_millions',
            y='yoy_growth_percent',
            size='market_share_percent',
            hover_data=['commodity'],
            title="YoY Growth vs Current Export Value",
            labels={'current_value_millions': 'Current Value ($M)', 'yoy_growth_percent': 'YoY Growth (%)'}
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Raw data tables
    st.markdown("---")
    st.subheader("📋 Raw Data Tables")
    
    tab1, tab2 = st.tabs(["Opportunities Data", "Opportunity Matrix"])
    
    with tab1:
        if opportunities_df is not None:
            st.dataframe(opportunities_df, use_container_width=True)
            st.download_button(
                "⬇️ Download CSV",
                opportunities_df.to_csv(index=False),
                "opportunities_data.csv",
                "text/csv"
            )
    
    with tab2:
        if matrix_df is not None:
            st.dataframe(matrix_df, use_container_width=True)
            st.download_button(
                "⬇️ Download CSV",
                matrix_df.to_csv(index=False),
                "opportunity_matrix.csv",
                "text/csv"
            )


# Footer
def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6B7280; padding: 2rem;'>
        <p><strong>Rwanda Export Strategy Dashboard</strong></p>
        <p>NISR Hackathon 2025 | Authors: Orpheus Mhizha Manga & Antony Wambugu</p>
        <p>Data-driven insights for Rwanda's export growth</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
    show_footer()
