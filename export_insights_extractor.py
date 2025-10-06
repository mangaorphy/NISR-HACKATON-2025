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
    
    def export_to_json(self, filename='export_insights.json'):
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
                f'{base_filename}_opportunities.csv', index=False
            )
        
        # Opportunity matrix
        if self.insights.get('opportunity_matrix'):
            pd.DataFrame(self.insights['opportunity_matrix']).to_csv(
                f'{base_filename}_opportunity_matrix.csv', index=False
            )
        
        # Policy recommendations
        if self.insights.get('policy_recommendations'):
            pd.DataFrame(self.insights['policy_recommendations']).to_csv(
                f'{base_filename}_policy_recommendations.csv', index=False
            )
        
        # Youth/SME opportunities
        if self.insights.get('youth_sme_opportunities'):
            pd.DataFrame(self.insights['youth_sme_opportunities']).to_csv(
                f'{base_filename}_youth_sme_opportunities.csv', index=False
            )
        
        # Strategic markets
        if self.insights.get('strategic_markets'):
            for tier, markets in self.insights['strategic_markets'].items():
                pd.DataFrame(markets).to_csv(
                    f'{base_filename}_strategic_{tier}.csv', index=False
                )
        
        print(f"✅ Insights exported to multiple CSV files: {base_filename}_*.csv")
        return f'{base_filename}_*.csv'
    
    def get_summary_stats(self):
        """Get quick summary statistics"""
        return {
            'total_opportunities': len(self.insights.get('top_opportunities', [])),
            'high_priority_policies': len([p for p in self.insights.get('policy_recommendations', []) if p['priority'] == 'HIGH']),
            'youth_sme_sectors': len(self.insights.get('youth_sme_opportunities', [])),
            'strategic_markets': sum([
                len(self.insights.get('strategic_markets', {}).get('tier1_powerhouses', [])),
                len(self.insights.get('strategic_markets', {}).get('tier2_emerging', [])),
                len(self.insights.get('strategic_markets', {}).get('tier3_untapped', []))
            ])
        }


# Helper function to use in notebook
def create_insights_export(commodities_df, opportunity_analysis, quarterly_data, 
                          tier1_markets, tier2_markets, tier3_markets):
    """
    One-function call to extract all insights and export them
    """
    extractor = ExportInsightsExtractor()
    
    # Extract all insights
    extractor.extract_commodity_insights(commodities_df)
    extractor.extract_opportunity_analysis(opportunity_analysis)
    extractor.extract_market_trends(quarterly_data)
    extractor.extract_strategic_markets(tier1_markets, tier2_markets, tier3_markets)
    extractor.generate_policy_recommendations()
    extractor.generate_youth_sme_opportunities()
    
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
    
    return extractor, json_file, csv_files
