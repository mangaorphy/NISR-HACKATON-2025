# 🗂️ File Organization Guide

## Quick Start

Run this single command to organize all your files:

```bash
cd /Users/cococe/Desktop/NISR-HACKATHON
./organize_files.sh
```

## What Will Happen

The script will:
1. ✅ **Create backup** of all CSV and JSON files
2. ✅ **Create organized folders**
3. ✅ **Move files** to appropriate locations
4. ✅ **Generate documentation** for the structure

## New Folder Structure

```
NISR-HACKATHON/
│
├── 📊 data/
│   ├── raw/              # Q3 2024 original NISR data
│   ├── wits/             # Historical WITS data (2018-2022)
│   ├── processed/        # Cleaned datasets
│   └── insights/         # Generated insights & forecasts
│
├── 📚 docs/              # All documentation
│
├── 🔧 scripts/           # Python scripts
│
├── 📓 import_export.ipynb
├── 🌐 dashboard_app.py
└── 📋 requirements.txt
```

## File Mappings

### Data Files

**Q3 2024 Raw Data** → `data/raw/`
- 2024Q3_ExportCountry.csv
- 2024Q3_ExportsCommodity.csv
- 2024Q3_ReexportsCommodity.csv
- 2024Q3_Regional blocks.csv
- 2024Q3_Trade by continents.csv
- 2024Q3_Trade_report_annexTables_0.xlsx - Total trade with the World.csv

**WITS Historical Data** → `data/wits/`
- rwanda_export_partners_2018_2022_combined.csv
- rwanda_exports_growth_analysis_2018_2022.csv
- rwanda_exports_regional_analysis_2018_2022.csv
- rwanda_exports_yearly_summary_2018_2022.csv

**Processed Data** → `data/processed/`
- analysis_ready_total_trade_world_updated.csv

**Insights** → `data/insights/`
- export_insights.json
- export_insights_*.csv (all insight files)

### Scripts

**Python Scripts** → `scripts/`
- combine_wits_partner_data.py
- export_insights_extractor.py

### Documentation

**Documentation** → `docs/`
- ADD_PREDICTIONS_TO_DASHBOARD.md
- COMPLETE_SOLUTION_OVERVIEW.md
- DASHBOARD_SETUP_GUIDE.md
- HACKATHON_PROJECT_SUMMARY.md
- HOW_TO_RUN_DASHBOARD.md
- PREDICTIVE_DASHBOARD_GUIDE.md
- PREDICTIVE_IMPLEMENTATION_SUMMARY.md
- SYSTEM_ARCHITECTURE.md

## After Organization

### Update Your Notebook

You'll need to update file paths in `import_export.ipynb`:

**Before:**
```python
commodities_df = pd.read_csv('2024Q3_ExportsCommodity.csv')
wits_data = pd.read_csv('rwanda_export_partners_2018_2022_combined.csv')
```

**After:**
```python
commodities_df = pd.read_csv('data/raw/2024Q3_ExportsCommodity.csv')
wits_data = pd.read_csv('data/wits/rwanda_export_partners_2018_2022_combined.csv')
```

### Update Dashboard

The dashboard app needs updated paths:

**Before:**
```python
with open('export_insights.json', 'r') as f:
```

**After:**
```python
with open('data/insights/export_insights.json', 'r') as f:
```

### Update Scripts

Scripts in the `/scripts` folder may need path updates:

```python
# Use relative paths from project root
import sys
sys.path.append('..')
```

## Safety Features

✅ **Automatic Backup**: All files backed up to `backup_before_organization/`  
✅ **Non-destructive**: Only moves files, doesn't delete anything  
✅ **Documentation**: Creates README files in data folders  
✅ **Reversible**: Keep backup until you confirm everything works

## Verification

After running the script, verify the structure:

```bash
# Check new structure
ls -R data/

# Verify backup
ls backup_before_organization/
```

## Rollback (If Needed)

If something goes wrong:

```bash
# Restore from backup
cp backup_before_organization/* .
```

## Benefits

✅ **Better readability** - Clear separation of concerns  
✅ **Easier navigation** - Find files quickly  
✅ **Professional structure** - Industry-standard organization  
✅ **Scalability** - Easy to add new data  
✅ **Version control** - Better Git management  
✅ **Collaboration** - Team members know where to find things

## Next Steps

1. Run the organization script
2. Update notebook file paths
3. Update dashboard file paths
4. Test that everything still works
5. Delete backup folder (after confirming)

---

**Ready to organize? Run:**
```bash
./organize_files.sh
```
