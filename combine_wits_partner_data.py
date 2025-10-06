#!/usr/bin/env python3
"""
WITS Partner Data Combination Script
Combines Rwanda's export partner data from 2018-2022 into a single comprehensive dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_and_combine_wits_data():
    """Load and combine all WITS partner data files"""
    
    print("🔄 COMBINING RWANDA WITS PARTNER DATA (2018-2022)")
    print("=" * 60)
    
    # File mapping
    files = {
        2018: "WITS-Partner_2018.xlsx - Partner.csv",
        2019: "WITS-Partner_2019.xlsx - Partner.csv", 
        2020: "WITS-Partner_2020.xlsx - Partner.csv",
        2021: "WITS-Partner_2021.xlsx - Partner.csv",
        2022: "WITS-Partner_2022.xlsx - Partner.csv"
    }
    
    combined_data = []
    
    for year, filename in files.items():
        try:
            print(f"📂 Loading {filename}...")
            df = pd.read_csv(filename)
            
            # Verify year column matches expected year
            df['Year'] = year  # Ensure consistency
            
            # Add transaction identifier
            df['Transaction_ID'] = df.apply(lambda row: f"RW-{row['Partner Name'][:3].upper()}-{year}", axis=1)
            
            # Clean data - remove rows with no export value
            df_clean = df[df['Export (US$ Thousand)'].notna() & (df['Export (US$ Thousand)'] != '')]
            
            print(f"   ✅ {len(df_clean)} records with export values loaded for {year}")
            combined_data.append(df_clean)
            
        except FileNotFoundError:
            print(f"   ❌ {filename} not found")
        except Exception as e:
            print(f"   ❌ Error loading {filename}: {e}")
    
    if not combined_data:
        print("❌ No data files could be loaded")
        return None
    
    # Combine all dataframes
    print(f"\n🔗 Combining {len(combined_data)} datasets...")
    combined_df = pd.concat(combined_data, ignore_index=True)
    
    # Data quality improvements
    print("🧹 Cleaning and enhancing data...")
    
    # Standardize partner names (remove extra spaces, etc.)
    combined_df['Partner Name'] = combined_df['Partner Name'].str.strip()
    
    # Convert numeric columns
    numeric_cols = ['Export (US$ Thousand)', 'Export Partner Share (%)', 
                   'Export Share in Total Products (%)', 'No Of exported HS6 digit Products']
    
    for col in numeric_cols:
        combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')
    
    # Add calculated fields
    combined_df['Export_Value_USD'] = combined_df['Export (US$ Thousand)'] * 1000  # Convert to actual USD
    combined_df['Export_Value_Millions'] = combined_df['Export (US$ Thousand)'] / 1000  # Convert to millions
    
    # Create regional groupings
    def assign_region(country):
        """Assign countries to regions"""
        africa_countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 
                          'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Congo, Rep.', 
                          'Congo, Dem. Rep.', 'Cote d\'Ivoire', 'Djibouti', 'Egypt, Arab Rep.', 'Equatorial Guinea',
                          'Eritrea', 'Eswatini', 'Ethiopia(excludes Eritrea)', 'Gabon', 'Gambia, The', 'Ghana',
                          'Guinea', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali',
                          'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
                          'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia',
                          'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda',
                          'Zambia', 'Zimbabwe']
        
        europe_countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
                          'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland',
                          'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia',
                          'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'North Macedonia',
                          'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'Serbia, FR(Serbia/Montenegro)',
                          'Slovak Republic', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']
        
        asia_countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei',
                         'Cambodia', 'China', 'Georgia', 'Hong Kong, China', 'India', 'Indonesia', 'Iran, Islamic Rep.',
                         'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Korea, Rep.', 'Korea, Dem. Rep.',
                         'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Lebanon', 'Macao', 'Malaysia', 'Mongolia',
                         'Myanmar', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia',
                         'Singapore', 'Sri Lanka', 'Syrian Arab Republic', 'Tajikistan', 'Thailand', 'Turkey',
                         'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
        
        americas_countries = ['Argentina', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica',
                            'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Jamaica', 'Mexico',
                            'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'United States', 'Uruguay', 'Venezuela']
        
        oceania_countries = ['Australia', 'Fiji', 'New Zealand', 'Papua New Guinea']
        
        if country in africa_countries:
            return 'Africa'
        elif country in europe_countries:
            return 'Europe & Central Asia'
        elif country in asia_countries:
            return 'Asia & Middle East'
        elif country in americas_countries:
            return 'Americas'
        elif country in oceania_countries:
            return 'Oceania'
        else:
            return 'Other/Regional Grouping'
    
    combined_df['Region'] = combined_df['Partner Name'].apply(assign_region)
    
    # Add growth calculations year-over-year
    print("📊 Calculating year-over-year growth rates...")
    
    def calculate_growth_rates(df):
        """Calculate YoY growth for each country"""
        df_sorted = df.sort_values(['Partner Name', 'Year'])
        df_sorted['YoY_Growth_Rate'] = df_sorted.groupby('Partner Name')['Export (US$ Thousand)'].pct_change() * 100
        df_sorted['YoY_Growth_Absolute'] = df_sorted.groupby('Partner Name')['Export (US$ Thousand)'].diff()
        return df_sorted
    
    combined_df = calculate_growth_rates(combined_df)
    
    # Summary statistics
    print(f"\n📈 COMBINED DATASET SUMMARY:")
    print(f"   • Total Records: {len(combined_df):,}")
    print(f"   • Years Covered: {combined_df['Year'].min()} - {combined_df['Year'].max()}")
    print(f"   • Unique Partners: {combined_df['Partner Name'].nunique()}")
    print(f"   • Total Export Value: ${combined_df['Export_Value_USD'].sum():,.0f}")
    
    # Top partners by total value
    top_partners = combined_df.groupby('Partner Name')['Export_Value_Millions'].sum().nlargest(10)
    print(f"\n🏆 TOP 10 EXPORT PARTNERS (2018-2022):")
    for i, (partner, value) in enumerate(top_partners.items(), 1):
        print(f"   {i:2d}. {partner}: ${value:.1f}M")
    
    return combined_df

def save_combined_data(df):
    """Save the combined dataset in multiple formats"""
    
    if df is None:
        return
    
    print(f"\n💾 SAVING COMBINED DATASET...")
    
    # Main combined file
    output_file = "rwanda_export_partners_2018_2022_combined.csv"
    df.to_csv(output_file, index=False)
    print(f"   ✅ Main dataset: {output_file}")
    
    # Summary by year
    yearly_summary = df.groupby('Year').agg({
        'Export_Value_Millions': ['sum', 'count'],
        'Partner Name': 'nunique',
        'No Of exported HS6 digit Products': 'sum'
    }).round(2)
    yearly_summary.columns = ['Total_Exports_M', 'Export_Transactions', 'Unique_Partners', 'Total_Products']
    yearly_summary.to_csv("rwanda_exports_yearly_summary_2018_2022.csv")
    print(f"   ✅ Yearly summary: rwanda_exports_yearly_summary_2018_2022.csv")
    
    # Regional analysis
    regional_summary = df.groupby(['Region', 'Year']).agg({
        'Export_Value_Millions': 'sum',
        'Partner Name': 'nunique'
    }).round(2)
    regional_summary.to_csv("rwanda_exports_regional_analysis_2018_2022.csv")
    print(f"   ✅ Regional analysis: rwanda_exports_regional_analysis_2018_2022.csv")
    
    # Growth analysis (countries with data in multiple years)
    growth_analysis = df[df['YoY_Growth_Rate'].notna()].copy()
    if not growth_analysis.empty:
        growth_summary = growth_analysis.groupby('Partner Name').agg({
            'YoY_Growth_Rate': ['mean', 'std', 'count'],
            'Export_Value_Millions': ['first', 'last']
        }).round(2)
        growth_summary.columns = ['Avg_Growth_Rate', 'Growth_Volatility', 'Years_of_Data', 'First_Year_Value', 'Last_Year_Value']
        growth_summary = growth_summary[growth_summary['Years_of_Data'] >= 2]  # Only countries with 2+ years
        growth_summary.to_csv("rwanda_exports_growth_analysis_2018_2022.csv")
        print(f"   ✅ Growth analysis: rwanda_exports_growth_analysis_2018_2022.csv")

def main():
    """Main execution function"""
    try:
        # Load and combine data
        combined_df = load_and_combine_wits_data()
        
        if combined_df is not None:
            # Save results
            save_combined_data(combined_df)
            
            print(f"\n🎉 SUCCESS! WITS partner data successfully combined!")
            print(f"📋 Ready for analysis in your hackathon notebook!")
            
        else:
            print(f"❌ Failed to combine data - check file availability")
            
    except Exception as e:
        print(f"❌ Error in main execution: {e}")

if __name__ == "__main__":
    main()