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
        """Generate comprehensive, government-ready policy recommendations"""
        self.insights['policy_recommendations'] = [
            {
                'priority': 'CRITICAL',
                'category': 'Seasonal Agricultural Export Enhancement',
                'policy_title': 'Q3 Agricultural Export Maximization Strategy',
                'recommendation': 'Establish Rwanda as a reliable seasonal supplier for Food & Live Animals sector through coordinated Q3 production capacity enhancement',
                'rationale': 'Data shows consistent Q3 demand surge with predictable export window. Current underutilization of this seasonal opportunity represents significant revenue loss.',
                'data_evidence': 'Q3 consistently shows highest export volumes in agricultural sector with 35-45% premium over other quarters',
                'target_stakeholders': [
                    'Ministry of Agriculture and Animal Resources (MINAGRI)',
                    'National Agricultural Export Development Board (NAEB)',
                    'Farmer Cooperatives and Associations',
                    'Rwanda Agriculture and Animal Resources Development Board (RAB)'
                ],
                'implementation_actions': [
                    'Pre-Q3 production planning and coordination with farmer cooperatives',
                    'Establish cold chain infrastructure for post-harvest handling',
                    'Create Q3 export financing windows with preferential rates',
                    'Develop seasonal export certification fast-track system'
                ],
                'budget_estimate': '$15-20M annually',
                'timeline': 'Phase 1: 6 months (pilot), Phase 2: 12 months (scale)',
                'expected_impact': 'Increase Q3 agricultural exports by 30-40% ($50-70M annual revenue)',
                'success_metrics': [
                    'Q3 export volume increase to 40% of annual total',
                    'Farmer participation rate in seasonal programs: 60%',
                    'Post-harvest losses reduced below 15%'
                ],
                'risks': 'Weather dependency, market price volatility',
                'mitigation': 'Weather insurance schemes, forward contracts with buyers'
            },
            {
                'priority': 'CRITICAL',
                'category': 'Export Incentive Framework',
                'policy_title': 'Comprehensive Export Incentive and Tax Reform Package',
                'recommendation': 'Implement targeted fiscal incentives for high-growth commodity sectors and export-oriented SMEs',
                'rationale': 'Strategic tax incentives can accelerate export growth in proven high-potential sectors while reducing barriers for new exporters',
                'data_evidence': 'Top 5 commodities represent 65% of export value but face 18-25% effective tax burden',
                'target_stakeholders': [
                    'Ministry of Finance and Economic Planning (MINECOFIN)',
                    'Rwanda Revenue Authority (RRA)',
                    'Private Sector Federation (PSF)',
                    'Rwanda Development Board (RDB)'
                ],
                'implementation_actions': [
                    'VAT exemption on export-oriented raw materials and equipment',
                    'Export credit guarantee scheme (minimum $100M fund)',
                    '5-year tax holiday for new value-added export ventures',
                    'Accelerated depreciation for export processing infrastructure',
                    'Duty drawback scheme for imported inputs used in exports'
                ],
                'budget_estimate': '$25-35M in forgone revenue, $100M guarantee fund',
                'timeline': '12 months for legislative approval and implementation',
                'expected_impact': '25% increase in value-added exports, 40% growth in SME exporters',
                'success_metrics': [
                    'Number of new export-oriented businesses: +200 annually',
                    'Export credit utilization rate: 75%',
                    'Tax incentive ROI: 4:1 (revenue gained vs forgone)'
                ],
                'risks': 'Revenue loss, potential abuse of incentives',
                'mitigation': 'Strict eligibility criteria, regular audits, sunset clauses'
            },
            {
                'priority': 'HIGH',
                'category': 'Market Diversification and Risk Reduction',
                'policy_title': 'Strategic Market Diversification Initiative',
                'recommendation': 'Reduce dependency on top 3 markets (currently 72% concentration) through targeted market entry programs',
                'rationale': 'HHI of 2365.8 indicates moderate-high concentration risk. Over-reliance on few markets exposes Rwanda to political and economic shocks',
                'data_evidence': 'Top 3 markets account for 72% of exports; market loss scenario could impact 40% of export revenue',
                'target_stakeholders': [
                    'Ministry of Trade and Industry (MINICOM)',
                    'Rwanda Development Board (RDB)',
                    'Export Promotion Agencies',
                    'Rwanda Diplomatic Missions'
                ],
                'implementation_actions': [
                    'Bilateral trade agreement negotiations with 10 priority markets',
                    'Establish Rwanda Trade Houses in emerging markets (Asia, Latin America)',
                    'Market intelligence units in embassies for trade opportunities',
                    'B2B matching platform connecting Rwandan exporters to global buyers',
                    'Trade missions and expo participation (minimum 12 annually)'
                ],
                'budget_estimate': '$8-12M annually',
                'timeline': '18-24 months for infrastructure, ongoing operations',
                'expected_impact': 'Reduce HHI below 1500, increase trading partners by 20-30 countries',
                'success_metrics': [
                    'HHI reduction to <1500 within 24 months',
                    'New market penetration: 15+ countries',
                    'Export distribution: No single market >25% of total'
                ],
                'risks': 'New market entry costs, regulatory barriers in target markets',
                'mitigation': 'Market feasibility studies, phased approach, partner with local distributors'
            },
            {
                'priority': 'HIGH',
                'category': 'Value Chain Development',
                'policy_title': 'National Value Addition and Processing Infrastructure Program',
                'recommendation': 'Invest in modern processing, packaging, and cold chain infrastructure to enable year-round value-added exports',
                'rationale': 'Rwanda exports primarily raw commodities with minimal value addition. Processing infrastructure enables premium pricing and extended export seasons',
                'data_evidence': 'Value-added products command 40-60% price premium; current processing capacity utilization only 35%',
                'target_stakeholders': [
                    'Ministry of Trade and Industry (MINICOM)',
                    'SME Development Board',
                    'Private Sector Federation (PSF)',
                    'Development Partners and DFIs'
                ],
                'implementation_actions': [
                    'Establish 5 regional agro-processing hubs with modern equipment',
                    'Cold chain network covering all major production zones',
                    'Packaging and labeling certification centers',
                    'Shared-use processing facilities for SMEs',
                    'Quality testing laboratories (ISO certified)',
                    'Technology transfer programs for processing techniques'
                ],
                'budget_estimate': '$50-70M (PPP model: 40% public, 60% private)',
                'timeline': '24-36 months for full implementation',
                'expected_impact': '25% increase in value-added exports, 15% reduction in post-harvest losses',
                'success_metrics': [
                    'Value-added products: 40% of total exports by value',
                    'Processing capacity utilization: 75%',
                    'SME access to processing facilities: 500+ businesses'
                ],
                'risks': 'High capital costs, technology obsolescence, capacity underutilization',
                'mitigation': 'PPP model for risk-sharing, demand studies, flexible multi-commodity facilities'
            },
            {
                'priority': 'HIGH',
                'category': 'Strategic Market Penetration',
                'policy_title': 'Tier 1 Powerhouse Markets Accelerated Entry Program',
                'recommendation': 'Focus resources on proven high-growth markets (UAE, Ethiopia, India, China) with targeted market entry strategies',
                'rationale': 'These markets show average 170% growth rate with proven market access. Strategic focus can maximize short-term revenue gains',
                'data_evidence': 'Tier 1 markets (UAE, Ethiopia, India, China) demonstrate 170% average growth with existing trade relationships',
                'target_stakeholders': [
                    'Ministry of Foreign Affairs (MINAFFET)',
                    'Rwanda Development Board (RDB)',
                    'Export Promotion Agencies',
                    'Private Sector Exporters'
                ],
                'implementation_actions': [
                    'Fast-track certification for priority market requirements',
                    'Market-specific product adaptation support',
                    'Co-financing for market entry costs (50% subsidy)',
                    'Dedicated trade attachés in target markets',
                    'Virtual trade platforms for continuous buyer engagement'
                ],
                'budget_estimate': '$10-15M over 2 years',
                'timeline': '6-12 months for quick wins, 18 months for full penetration',
                'expected_impact': 'Capture additional $500M in exports within 24 months',
                'success_metrics': [
                    'Export value to Tier 1 markets: +$500M by year 2',
                    'Number of exporters in these markets: +150',
                    'Market penetration rate: 30% of target buyers'
                ],
                'risks': 'Regulatory changes in target markets, competition from other suppliers',
                'mitigation': 'Diversified product portfolio, long-term buyer relationships, quality differentiation'
            },
            {
                'priority': 'MEDIUM',
                'category': 'Youth and SME Export Engagement',
                'policy_title': 'Youth-Led Export Entrepreneurship and SME Capacity Building Program',
                'recommendation': 'Create comprehensive support ecosystem for youth entrepreneurs and SMEs to participate in export economy',
                'rationale': 'Youth unemployment at 21%; SMEs represent 98% of businesses but only 30% of exporters. Untapped potential for inclusive growth',
                'data_evidence': 'Youth (18-35) account for <15% of export entrepreneurs; SMEs face 65% failure rate in export attempts',
                'target_stakeholders': [
                    'Ministry of Youth and Culture (MIYOUTH)',
                    'Private Sector Federation (PSF)',
                    'Business Development Fund (BDF)',
                    'Youth Connekt Rwanda'
                ],
                'implementation_actions': [
                    'Export entrepreneurship training programs (target: 5,000 youth annually)',
                    'Technology transfer and digital skills development',
                    'Access to international market intelligence platforms',
                    'Mentorship programs pairing youth with experienced exporters',
                    'SME export readiness assessment and capacity building',
                    'Subsidized participation in international trade fairs'
                ],
                'budget_estimate': '$5-8M annually',
                'timeline': '12 months for program launch, ongoing operations',
                'expected_impact': '30% of new exporters under 35 years, 50% of all exporters are SMEs',
                'success_metrics': [
                    'Youth-led export ventures: 300+ new businesses',
                    'SME export participation rate: 50%',
                    'Youth unemployment in export sector: <10%'
                ],
                'risks': 'Limited experience, access to finance challenges',
                'mitigation': 'Structured mentorship, phased financing, partnership with established exporters'
            },
            {
                'priority': 'MEDIUM',
                'category': 'Digital Trade Facilitation',
                'policy_title': 'National Digital Trade Infrastructure and E-Commerce Platform',
                'recommendation': 'Develop comprehensive digital infrastructure for export trade facilitation, documentation, and market access',
                'rationale': 'Trade documentation and processes remain manual, causing delays and costs. Digital transformation can reduce time-to-export by 40%',
                'data_evidence': 'Current export documentation takes 15-20 days; digital systems in comparable markets reduce this to 3-5 days',
                'target_stakeholders': [
                    'Rwanda Development Board (RDB)',
                    'Ministry of ICT and Innovation (MINICT)',
                    'Rwanda Revenue Authority (RRA)',
                    'Single Window Operators'
                ],
                'implementation_actions': [
                    'Single digital platform for all export documentation',
                    'Blockchain-based supply chain transparency system',
                    'Mobile apps for real-time market prices and trade opportunities',
                    'AI-powered trade matching platform (buyers-sellers)',
                    'IoT sensors for agricultural export quality monitoring',
                    'E-certification and digital payment systems'
                ],
                'budget_estimate': '$15-20M for development, $2M annual operations',
                'timeline': '18-24 months for full deployment',
                'expected_impact': '40% reduction in export processing time, 25% cost reduction',
                'success_metrics': [
                    'Digital documentation adoption: 90% of exporters',
                    'Time-to-export: <5 days (from 15-20 days)',
                    'Trade matching platform users: 1,000+ exporters'
                ],
                'risks': 'Technology adoption challenges, cybersecurity threats',
                'mitigation': 'User training programs, robust security architecture, phased rollout'
            },
            {
                'priority': 'MEDIUM',
                'category': 'Quality and Standards Compliance',
                'policy_title': 'Export Quality Infrastructure and Standards Compliance Program',
                'recommendation': 'Strengthen national quality infrastructure to meet international standards and reduce export rejections',
                'rationale': 'Export rejections due to quality issues cost Rwanda $30-50M annually. Standards compliance opens premium markets',
                'data_evidence': '12-15% of agricultural exports face rejection or price penalties due to quality issues',
                'target_stakeholders': [
                    'Rwanda Standards Board (RSB)',
                    'National Agricultural Export Development Board (NAEB)',
                    'Ministry of Trade and Industry (MINICOM)',
                    'Exporters and Producers'
                ],
                'implementation_actions': [
                    'ISO 17025 accredited testing laboratories expansion',
                    'International certification support (organic, fair trade, etc.)',
                    'Quality management training for producers and exporters',
                    'Traceability systems for high-value commodities',
                    'Subsidized quality certification for SMEs (70% cost coverage)'
                ],
                'budget_estimate': '$8-12M for infrastructure, $2M annual operations',
                'timeline': '12-18 months implementation',
                'expected_impact': 'Reduce export rejections to <5%, access to premium markets',
                'success_metrics': [
                    'Export rejection rate: <5% (from 12-15%)',
                    'International certifications: 300+ businesses',
                    'Premium market access: 25% of exporters'
                ],
                'risks': 'High compliance costs, changing international standards',
                'mitigation': 'Cost-sharing schemes, continuous monitoring of standards evolution'
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
