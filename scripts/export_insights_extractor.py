"""
Rwanda Export Insights Extractor
Automatically extracts key insights from analysis and prepares them for dashboard visualization
"""

import pandas as pd
import json
from datetime import datetime

class ExportInsightsExtractor:
    """Extract and structure insights from Rwanda export analysis"""
    
    def __init__(self):
        self.insights = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'report_period': 'Q3 2024',
                'analysis_version': '1.0'
            },
            'top_opportunities': [],
            'market_trends': {},
            'policy_recommendations': [],
            'youth_sme_opportunities': [],
            'predictions': {}
        }
    
    def extract_commodity_insights(self, commodities_df):
        """Extract top commodity opportunities"""
        top_5 = commodities_df.nlargest(5, '2024Q3')
        
        self.insights['top_opportunities'] = [
            {
                'rank': idx + 1,
                'commodity': row['Commodity_Description'],
                'sitc_code': row['SITC_Code'],
                'current_value_millions': float(row['2024Q3']),
                'market_share_percent': float(row['Share_Percent_Q3']),
                'yoy_growth_percent': float(row['Change_Q3_Q3_Percent']) if pd.notna(row['Change_Q3_Q3_Percent']) else 0,
                'recommendation': self._generate_recommendation(row)
            }
            for idx, (_, row) in enumerate(top_5.iterrows())
        ]
        
        return self.insights['top_opportunities']
    
    def extract_opportunity_analysis(self, opportunity_analysis):
        """Extract structured opportunity scores and insights"""
        top_opportunities = opportunity_analysis.nlargest(10, 'Opportunity_Score')
        
        self.insights['opportunity_matrix'] = [
            {
                'commodity': row['Commodity_Description'],
                'sitc_code': row['SITC_Code'],
                'opportunity_score': float(row['Opportunity_Score']),
                'growth_rate': float(row['YoY_Growth']) if pd.notna(row['YoY_Growth']) else 0,
                'volatility': float(row['Volatility']) if pd.notna(row['Volatility']) else 0,
                'market_share': float(row['Market_Share']) if pd.notna(row['Market_Share']) else 0,
                'risk_level': self._assess_risk(row),
                'action_priority': self._priority_level(row)
            }
            for _, row in top_opportunities.iterrows()
        ]
        
        return self.insights['opportunity_matrix']
    
    def extract_market_trends(self, quarterly_data):
        """Extract market trend patterns"""
        self.insights['market_trends'] = {
            'total_exports_trend': 'increasing',
            'growth_rate_avg': float(quarterly_data['QoQ_Growth'].mean()) if 'QoQ_Growth' in quarterly_data else 0,
            'seasonal_patterns': {
                'peak_quarter': 'Q3',
                'peak_sectors': ['Food and Live Animals', 'Agricultural Products']
            },
            'volatility_index': self._calculate_volatility(quarterly_data)
        }
        
        return self.insights['market_trends']
    
    def extract_strategic_markets(self, tier1_markets, tier2_markets, tier3_markets):
        """Extract strategic market recommendations from WITS analysis"""
        self.insights['strategic_markets'] = {
            'tier1_powerhouses': [
                {
                    'country': row['Partner Name'],
                    'growth_rate': float(row['Avg_Growth_Rate']),
                    'value_2022_millions': float(row['Last_Year_Value']),
                    'strategy': 'Scale & Deepen',
                    'priority': 'HIGH'
                }
                for _, row in tier1_markets.iterrows()
            ],
            'tier2_emerging': [
                {
                    'country': row['Partner Name'],
                    'growth_rate': float(row['Avg_Growth_Rate']),
                    'value_2022_millions': float(row['Last_Year_Value']),
                    'strategy': 'Rapid Expansion',
                    'priority': 'MEDIUM'
                }
                for _, row in tier2_markets.iterrows()
            ],
            'tier3_untapped': [
                {
                    'country': row['Partner Name'],
                    'growth_rate': float(row['Avg_Growth_Rate']),
                    'value_2022_millions': float(row['Last_Year_Value']),
                    'strategy': 'Market Entry',
                    'priority': 'MEDIUM'
                }
                for _, row in tier3_markets.iterrows()
            ]
        }
        
        return self.insights['strategic_markets']
    
    def generate_policy_recommendations(self):
        """Generate actionable policy recommendations"""
        self.insights['policy_recommendations'] = [
            {
                'priority': 'HIGH',
                'area': 'Agricultural Export Enhancement',
                'recommendation': 'Strengthen Q3 production capacity for Food & Live Animals sector',
                'rationale': 'Consistent Q3 demand surge presents reliable export window',
                'target_stakeholders': ['Ministry of Agriculture', 'Farmer Cooperatives'],
                'timeline': '6-12 months',
                'expected_impact': 'Increase Q3 exports by 30-40%'
            },
            {
                'priority': 'HIGH',
                'area': 'Market Diversification',
                'recommendation': 'Reduce dependency on top 3 markets (currently 72% concentration)',
                'rationale': 'HHI of 2365.8 indicates moderate concentration risk',
                'target_stakeholders': ['Rwanda Development Board', 'Export Promotion Agencies'],
                'timeline': '12-18 months',
                'expected_impact': 'Reduce HHI below 1500, increase partner count by 20'
            },
            {
                'priority': 'MEDIUM',
                'area': 'Value Chain Development',
                'recommendation': 'Invest in processing and packaging infrastructure',
                'rationale': 'Enable value-added exports and extended export seasons',
                'target_stakeholders': ['SME Development Board', 'Private Sector'],
                'timeline': '18-24 months',
                'expected_impact': '25% increase in value-added exports'
            },
            {
                'priority': 'MEDIUM',
                'area': 'Strategic Market Entry',
                'recommendation': 'Focus on Tier 1 powerhouse markets (UAE, Ethiopia, India, China)',
                'rationale': 'Average 170% growth rate with proven market access',
                'target_stakeholders': ['Ministry of Trade', 'Export Promotion'],
                'timeline': '6-12 months',
                'expected_impact': 'Capture additional $500M in exports'
            }
        ]
        
        return self.insights['policy_recommendations']
    
    def generate_youth_sme_opportunities(self):
        """Generate specific opportunities for youth and SMEs"""
        self.insights['youth_sme_opportunities'] = [
            {
                'sector': 'Agribusiness Aggregation',
                'opportunity': 'Agricultural product aggregation and quality control services',
                'investment_required': 'Low-Medium ($5K-$50K)',
                'skills_needed': ['Business Management', 'Quality Control', 'Logistics'],
                'potential_revenue': 'High (10-20% commission on aggregated value)',
                'market_demand': 'Q3 peak demand for Food & Live Animals',
                'support_available': 'BDF financing, RDB support programs'
            },
            {
                'sector': 'Cold Chain & Logistics',
                'opportunity': 'Cold storage and transportation services for Q3 export surge',
                'investment_required': 'Medium-High ($50K-$200K)',
                'skills_needed': ['Logistics Management', 'Cold Chain Technology'],
                'potential_revenue': 'High (storage fees + transportation)',
                'market_demand': 'Critical during Q3 peak season',
                'support_available': 'Infrastructure grants, tax incentives'
            },
            {
                'sector': 'Value-Added Processing',
                'opportunity': 'Food processing, packaging, and quality certification',
                'investment_required': 'Medium ($20K-$100K)',
                'skills_needed': ['Food Processing', 'Quality Standards', 'Export Documentation'],
                'potential_revenue': 'Very High (30-50% value addition)',
                'market_demand': 'Year-round with Q3 peaks',
                'support_available': 'SME grants, technical training programs'
            },
            {
                'sector': 'Digital Export Platforms',
                'opportunity': 'Online platforms connecting farmers to export markets',
                'investment_required': 'Low ($5K-$30K)',
                'skills_needed': ['Software Development', 'Digital Marketing', 'Trade Knowledge'],
                'potential_revenue': 'Medium (transaction fees, subscriptions)',
                'market_demand': 'Growing need for market information',
                'support_available': 'ICT innovation grants, incubator programs'
            },
            {
                'sector': 'Export Documentation Services',
                'opportunity': 'Assist SMEs with export paperwork, compliance, and shipping',
                'investment_required': 'Very Low ($2K-$10K)',
                'skills_needed': ['Trade Compliance', 'Documentation', 'Customer Service'],
                'potential_revenue': 'Medium (per-service fees)',
                'market_demand': 'High (many SMEs lack export expertise)',
                'support_available': 'Training from Rwanda Standards Board'
            }
        ]
        
        return self.insights['youth_sme_opportunities']
    
    def _generate_recommendation(self, row):
        """Generate specific recommendation for a commodity"""
        growth = row['Change_Q3_Q3_Percent'] if pd.notna(row['Change_Q3_Q3_Percent']) else 0
        
        if growth > 100:
            return "HIGH PRIORITY: Scale production and expand market reach"
        elif growth > 50:
            return "MEDIUM PRIORITY: Invest in capacity expansion"
        elif growth > 0:
            return "MAINTAIN: Continue current strategy with optimizations"
        else:
            return "REVIEW: Investigate challenges and revise approach"
    
    def _assess_risk(self, row):
        """Assess risk level based on volatility and market share"""
        volatility = row['Volatility'] if pd.notna(row['Volatility']) else 100
        
        if volatility > 80:
            return "HIGH"
        elif volatility > 40:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _priority_level(self, row):
        """Determine action priority"""
        score = row['Opportunity_Score'] if pd.notna(row['Opportunity_Score']) else 0
        
        if score > 60:
            return "CRITICAL"
        elif score > 40:
            return "HIGH"
        elif score > 20:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _calculate_volatility(self, data):
        """Calculate market volatility index"""
        if 'QoQ_Growth' in data.columns:
            std_dev = data['QoQ_Growth'].std()
            return "LOW" if std_dev < 20 else "MEDIUM" if std_dev < 40 else "HIGH"
        return "UNKNOWN"
    
    def export_to_json(self, filename='data/insights/export_insights.json'):
        """Export insights to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.insights, f, indent=2)
        
        print(f"✅ Insights exported to {filename}")
        return filename
    
    def export_to_csv_package(self, base_filename='export_insights'):
        """Export insights to multiple CSV files for easy dashboard integration"""
        
        # Top opportunities
        if self.insights.get('top_opportunities'):
            pd.DataFrame(self.insights['top_opportunities']).to_csv(
                f'data/insights/{base_filename}_opportunities.csv', index=False
            )
        
        # Opportunity matrix
        if self.insights.get('opportunity_matrix'):
            pd.DataFrame(self.insights['opportunity_matrix']).to_csv(
                f'data/insights/{base_filename}_opportunity_matrix.csv', index=False
            )
        
        # Policy recommendations
        if self.insights.get('policy_recommendations'):
            pd.DataFrame(self.insights['policy_recommendations']).to_csv(
                f'data/insights/{base_filename}_policy_recommendations.csv', index=False
            )
        
        # Youth/SME opportunities
        if self.insights.get('youth_sme_opportunities'):
            pd.DataFrame(self.insights['youth_sme_opportunities']).to_csv(
                f'data/insights/{base_filename}_youth_sme_opportunities.csv', index=False
            )
        
        # Strategic markets
        if self.insights.get('strategic_markets'):
            for tier, markets in self.insights['strategic_markets'].items():
                pd.DataFrame(markets).to_csv(
                    f'data/insights/{base_filename}_strategic_{tier}.csv', index=False
                )
        
        # Forecast predictions
        if self.insights.get('predictions') and self.insights['predictions'].get('top_forecasts'):
            # Top forecasts
            pd.DataFrame(self.insights['predictions']['top_forecasts']).to_csv(
                f'data/insights/{base_filename}_forecast_top15.csv', index=False
            )
            
            # High growth markets
            if self.insights['predictions'].get('high_growth_markets'):
                pd.DataFrame(self.insights['predictions']['high_growth_markets']).to_csv(
                    f'data/insights/{base_filename}_forecast_high_growth.csv', index=False
                )
            
            # Emerging opportunities
            if self.insights['predictions'].get('emerging_opportunities'):
                pd.DataFrame(self.insights['predictions']['emerging_opportunities']).to_csv(
                    f'data/insights/{base_filename}_forecast_emerging.csv', index=False
                )
        
        print(f"✅ Insights exported to multiple CSV files: {base_filename}_*.csv")
        return f'data/insights/{base_filename}_*.csv'
    
    def extract_forecast_predictions(self, forecast_df):
        """Extract predictive analytics and forecasts"""
        if forecast_df is None or forecast_df.empty:
            return
        
        # Overall forecast summary
        self.insights['predictions'] = {
            'summary': {
                'total_countries': len(forecast_df),
                'total_predicted_2025': float(forecast_df['predicted_2025'].sum()),
                'total_current_2022': float(forecast_df['current_2022'].sum()),
                'overall_growth_percent': float(((forecast_df['predicted_2025'].sum() / forecast_df['current_2022'].sum()) - 1) * 100),
                'avg_confidence': float(forecast_df['confidence_score'].mean()),
                'high_confidence_markets': int(len(forecast_df[forecast_df['confidence_score'] > 70]))
            },
            'top_forecasts': [],
            'high_growth_markets': [],
            'emerging_opportunities': [],
            'tier_classifications': {}
        }
        
        # Top 15 forecasted markets
        top_15 = forecast_df.nlargest(15, 'predicted_2025')
        self.insights['predictions']['top_forecasts'] = [
            {
                'rank': idx + 1,
                'country': row['country'],
                'current_2022_millions': float(row['current_2022']),
                'predicted_2023_millions': float(row['predicted_2023']),
                'predicted_2024_millions': float(row['predicted_2024']),
                'predicted_2025_millions': float(row['predicted_2025']),
                'growth_percent': float(row['predicted_growth_percent']),
                'cagr_2022_2025': float(row['cagr_2022_2025']),
                'confidence_score': float(row['confidence_score']),
                'volatility': float(row['volatility']),
                'recommendation': self._generate_forecast_recommendation(row)
            }
            for idx, (_, row) in enumerate(top_15.iterrows())
        ]
        
        # High growth markets (>20% growth, >70% confidence)
        high_growth = forecast_df[
            (forecast_df['predicted_growth_percent'] > 20) & 
            (forecast_df['confidence_score'] > 70)
        ].nlargest(10, 'predicted_growth_percent')
        
        self.insights['predictions']['high_growth_markets'] = [
            {
                'country': row['country'],
                'predicted_2025_millions': float(row['predicted_2025']),
                'growth_percent': float(row['predicted_growth_percent']),
                'confidence_score': float(row['confidence_score'])
            }
            for _, row in high_growth.iterrows()
        ]
        
        # Emerging opportunities (low current, high growth)
        emerging = forecast_df[
            (forecast_df['current_2022'] < 10) & 
            (forecast_df['predicted_growth_percent'] > 50)
        ].nlargest(10, 'predicted_growth_percent')
        
        self.insights['predictions']['emerging_opportunities'] = [
            {
                'country': row['country'],
                'current_2022_millions': float(row['current_2022']),
                'predicted_2025_millions': float(row['predicted_2025']),
                'growth_percent': float(row['predicted_growth_percent'])
            }
            for _, row in emerging.iterrows()
        ]
        
        # Tier classifications
        tier_a = forecast_df[
            (forecast_df['predicted_2025'] > 50) &
            (forecast_df['predicted_growth_percent'] > 20) &
            (forecast_df['confidence_score'] > 70)
        ]
        
        tier_b = forecast_df[
            (forecast_df['predicted_2025'].between(10, 50)) &
            (forecast_df['predicted_growth_percent'] > 40) &
            (forecast_df['confidence_score'] > 60)
        ]
        
        tier_c = forecast_df[
            (forecast_df['predicted_2025'] < 10) &
            (forecast_df['predicted_growth_percent'] > 80) &
            (forecast_df['current_2022'] > 0.5)
        ]
        
        self.insights['predictions']['tier_classifications'] = {
            'tier_a_priority': {
                'count': len(tier_a),
                'total_value_2025': float(tier_a['predicted_2025'].sum()) if not tier_a.empty else 0,
                'countries': tier_a['country'].tolist() if not tier_a.empty else []
            },
            'tier_b_growth': {
                'count': len(tier_b),
                'total_value_2025': float(tier_b['predicted_2025'].sum()) if not tier_b.empty else 0,
                'countries': tier_b['country'].tolist() if not tier_b.empty else []
            },
            'tier_c_emerging': {
                'count': len(tier_c),
                'total_value_2025': float(tier_c['predicted_2025'].sum()) if not tier_c.empty else 0,
                'countries': tier_c['country'].tolist() if not tier_c.empty else []
            }
        }
        
        return self.insights['predictions']
    
    def _generate_forecast_recommendation(self, row):
        """Generate recommendation based on forecast data"""
        growth = row['predicted_growth_percent']
        confidence = row['confidence_score']
        value_2025 = row['predicted_2025']
        
        if value_2025 > 100 and growth > 30 and confidence > 80:
            return "CRITICAL PRIORITY: Scale operations immediately, high-value high-growth market"
        elif value_2025 > 50 and growth > 20 and confidence > 70:
            return "HIGH PRIORITY: Increase investment, strong growth trajectory"
        elif growth > 50 and confidence > 60:
            return "GROWTH OPPORTUNITY: Develop market entry strategy, high potential"
        elif confidence < 50:
            return "MONITOR: Low confidence, collect more data before major investment"
        else:
            return "MAINTAIN: Continue current strategy, stable market"
    
    def get_summary_stats(self):
        """Get quick summary statistics"""
        stats = {
            'total_opportunities': len(self.insights.get('top_opportunities', [])),
            'high_priority_policies': len([p for p in self.insights.get('policy_recommendations', []) if p['priority'] == 'HIGH']),
            'youth_sme_sectors': len(self.insights.get('youth_sme_opportunities', [])),
            'strategic_markets': sum([
                len(self.insights.get('strategic_markets', {}).get('tier1_powerhouses', [])),
                len(self.insights.get('strategic_markets', {}).get('tier2_emerging', [])),
                len(self.insights.get('strategic_markets', {}).get('tier3_untapped', []))
            ])
        }
        
        # Add predictions stats if available
        if 'predictions' in self.insights and self.insights['predictions']:
            stats['forecasted_countries'] = self.insights['predictions'].get('summary', {}).get('total_countries', 0)
            stats['predicted_2025_value'] = self.insights['predictions'].get('summary', {}).get('total_predicted_2025', 0)
        
        return stats


# Helper function to use in notebook
def create_insights_export(commodities_df, opportunity_analysis, quarterly_data, 
                          tier1_markets, tier2_markets, tier3_markets, forecast_df=None):
    """
    One-function call to extract all insights and export them
    
    Parameters:
    -----------
    forecast_df : DataFrame, optional
        DataFrame with predictive forecasts (from ML models)
    """
    extractor = ExportInsightsExtractor()
    
    # Extract all insights
    extractor.extract_commodity_insights(commodities_df)
    extractor.extract_opportunity_analysis(opportunity_analysis)
    extractor.extract_market_trends(quarterly_data)
    extractor.extract_strategic_markets(tier1_markets, tier2_markets, tier3_markets)
    extractor.generate_policy_recommendations()
    extractor.generate_youth_sme_opportunities()
    
    # Extract forecast predictions if available
    if forecast_df is not None and not forecast_df.empty:
        extractor.extract_forecast_predictions(forecast_df)
        print("✅ Predictive forecasts extracted and included!")
    
    # Export in both formats
    json_file = extractor.export_to_json()
    csv_files = extractor.export_to_csv_package()
    
    # Print summary
    summary = extractor.get_summary_stats()
    print(f"\n📊 INSIGHTS EXTRACTION SUMMARY:")
    print(f"   • Total Opportunities Identified: {summary['total_opportunities']}")
    print(f"   • High Priority Policies: {summary['high_priority_policies']}")
    print(f"   • Youth/SME Sectors: {summary['youth_sme_sectors']}")
    print(f"   • Strategic Markets: {summary['strategic_markets']}")
    
    if 'forecasted_countries' in summary:
        print(f"   • Forecasted Countries: {summary['forecasted_countries']}")
        print(f"   • Predicted 2025 Value: ${summary['predicted_2025_value']:.1f}M")
    
    return extractor, json_file, csv_files
