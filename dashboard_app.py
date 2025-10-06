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
        with open('export_insights.json', 'r') as f:
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
    page = st.sidebar.radio(
        "Select View",
        ["📊 Executive Summary", "🎯 Top Opportunities", "🌍 Strategic Markets", 
         "📜 Policy Recommendations", "👥 Youth & SME Opportunities", "📈 Detailed Analytics"]
    )
    
    # Display metadata
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Report Period:** {insights['metadata']['report_period']}")
    st.sidebar.markdown(f"**Generated:** {insights['metadata']['generated_at'][:10]}")
    
    # Page routing
    if page == "📊 Executive Summary":
        show_executive_summary(insights)
    elif page == "🎯 Top Opportunities":
        show_top_opportunities(insights)
    elif page == "🌍 Strategic Markets":
        show_strategic_markets(insights)
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
    opp_df = load_csv_data('export_insights_opportunity_matrix.csv')
    
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
    tab1, tab2, tab3 = st.tabs(["🏆 Tier 1: Powerhouses", "🚀 Tier 2: Emerging", "💡 Tier 3: Untapped"])
    
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
        
        with st.expander(f"{'🔴' if policy['priority']=='HIGH' else '🟡' if policy['priority']=='MEDIUM' else '🟢'} {policy['area']}", expanded=policy['priority']=='HIGH'):
            st.markdown(f"**Priority:** <span class='{priority_class}'>{policy['priority']}</span>", unsafe_allow_html=True)
            st.markdown(f"**Recommendation:** {policy['recommendation']}")
            st.markdown(f"**Rationale:** {policy['rationale']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Stakeholders:** {', '.join(policy['target_stakeholders'])}")
                st.markdown(f"**Timeline:** {policy['timeline']}")
            with col2:
                st.markdown(f"**Expected Impact:** {policy['expected_impact']}")
    
    # Summary visualization
    st.markdown("---")
    st.subheader("📊 Policy Priority Distribution")
    
    priority_counts = pd.DataFrame(policies)['priority'].value_counts()
    fig = px.pie(
        values=priority_counts.values,
        names=priority_counts.index,
        title="Policy Recommendations by Priority",
        color_discrete_map={'HIGH': '#DC2626', 'MEDIUM': '#F59E0B', 'LOW': '#10B981'}
    )
    st.plotly_chart(fig, use_container_width=True)


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
    opportunities_df = load_csv_data('export_insights_opportunities.csv')
    matrix_df = load_csv_data('export_insights_opportunity_matrix.csv')
    
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
