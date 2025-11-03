# Sector Analysis Templates

This directory contains templates and tools for conducting comprehensive sector analysis.

## Contents

### Python Scripts
- **sector_analysis.py**: Main toolkit with classes and functions for financial analysis
- **bloomberg_data_extraction.py**: Helper script for Bloomberg Terminal data extraction

### Documentation
- **data_collection_template.md**: Checklist for data collection from Bloomberg
- **excel_model_guide.md**: Comprehensive guide for Excel financial modeling

## Quick Start

### 1. Set Up Python Environment
```bash
pip install pandas numpy matplotlib seaborn plotly
pip install openpyxl xlsxwriter
```

### 2. Prepare Your Data
- Extract data from Bloomberg Terminal using the field list in `bloomberg_data_extraction.py`
- Save raw data to `../data/raw/`
- Use the checklist in `data_collection_template.md`

### 3. Run Analysis
```python
from sector_analysis import SectorAnalysis

# Initialize
analysis = SectorAnalysis(data_path='../data/processed')

# Load data
analysis.load_data()

# Calculate ratios
ratios = analysis.calculate_ratios(analysis.financials_df)

# Generate report
analysis.generate_report(output_path='../reports')
```

### 4. Build Excel Model
- Follow the structure outlined in `excel_model_guide.md`
- Use Bloomberg Excel formulas provided
- Apply best practices for formatting and documentation

## File Organization

Your project directory should look like:
```
finance-projects/
├── SECTOR_ANALYSIS_GUIDE.md         (Main guide)
├── templates/
│   ├── python/
│   │   ├── sector_analysis.py
│   │   └── bloomberg_data_extraction.py
│   ├── excel_model_guide.md
│   ├── data_collection_template.md
│   └── README.md (this file)
├── data/
│   ├── raw/                          (Bloomberg exports)
│   ├── processed/                    (Cleaned data)
│   └── external/                     (Other sources)
├── analysis/
│   ├── python/                       (Your analysis scripts)
│   └── excel/                        (Your Excel models)
├── reports/
│   ├── drafts/
│   └── final/
└── references/                       (Industry reports, papers)
```

## Usage Examples

### Calculate Financial Ratios
```python
from sector_analysis import SectorAnalysis
import pandas as pd

# Load your financial data
df = pd.read_excel('../data/processed/financials.xlsx')

# Initialize analysis
analysis = SectorAnalysis(data_path='../data/processed')

# Calculate ratios
ratios = analysis.calculate_ratios(df)
print(ratios.head())
```

### DCF Valuation
```python
# 5-year FCF forecast (in millions)
fcf_forecast = [100, 110, 121, 133, 146]

# Valuation parameters
wacc = 0.10              # 10%
terminal_growth = 0.02   # 2%
net_debt = 500           # $500M
shares = 100             # 100M shares

# Run DCF
valuation = analysis.dcf_valuation(
    fcf_forecast=fcf_forecast,
    wacc=wacc,
    terminal_growth=terminal_growth,
    net_debt=net_debt,
    shares=shares
)

print(f"Fair Value: ${valuation['Price_Per_Share']:.2f}")
```

### Peer Comparison
```python
# Compare companies
companies = ['Company A', 'Company B', 'Company C']
metrics = ['Revenue', 'EBITDA_Margin', 'ROE', 'PE_Ratio']

fig = analysis.peer_comparison(companies, metrics)
fig.savefig('../reports/peer_comparison.png')
```

### Risk Analysis
```python
import numpy as np

# Calculate returns from price data
prices = analysis.prices_df['Price'].values
returns = np.diff(prices) / prices[:-1]

# Get risk metrics
risk_metrics = analysis.risk_metrics(returns)
print(risk_metrics)
```

## Bloomberg Terminal Tips

### Essential Functions
- `COMP <TICKER>` - Company overview
- `FA <TICKER>` - Financial analysis
- `RV <TICKER>` - Relative valuation
- `PEER <TICKER>` - Peer analysis
- `BI <SECTOR>` - Industry analysis

### Data Export
1. Create company list in `PORT` function
2. Use `FMAP` to map fields
3. Export using Excel Add-in (BDP/BDH functions)
4. Save to `data/raw/` with date stamp

### Excel Formulas
```excel
=BDP("AAPL US Equity", "PX_LAST")
=BDH("AAPL US Equity", "PX_LAST", TODAY()-365, TODAY())
```

## Best Practices

### Data Management
1. Always keep raw data unchanged
2. Create processed/cleaned versions in `data/processed/`
3. Document all data transformations
4. Include data source and extraction date in filenames
5. Regular backups

### Code Organization
1. Use the provided `SectorAnalysis` class as base
2. Create your own derived classes for specific sectors
3. Keep analysis scripts in `analysis/python/`
4. Use meaningful variable names
5. Comment your code

### Excel Models
1. Follow the structure in `excel_model_guide.md`
2. Use consistent color coding
3. Document all assumptions
4. Include data validation
5. Add error checks

## Customization

### Extending the Python Toolkit
```python
from sector_analysis import SectorAnalysis

class TechSectorAnalysis(SectorAnalysis):
    """Extended analysis for Technology sector"""
    
    def calculate_saas_metrics(self, df):
        """Calculate SaaS-specific metrics"""
        metrics = pd.DataFrame()
        metrics['ARR'] = df['Revenue']  # Annual Recurring Revenue
        metrics['CAC'] = df['Sales_Marketing'] / df['New_Customers']
        metrics['LTV'] = df['ARPU'] * df['Customer_Lifetime']
        metrics['LTV_CAC_Ratio'] = metrics['LTV'] / metrics['CAC']
        return metrics
```

### Adding Custom Visualizations
```python
def custom_chart(data):
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(12, 6))
    # Your custom visualization
    ax.plot(data)
    return fig
```

## Troubleshooting

### Common Issues

**Issue**: "Module not found"
**Solution**: Install required packages: `pip install pandas numpy matplotlib seaborn`

**Issue**: "File not found"
**Solution**: Check file paths are correct and files exist in `data/` directory

**Issue**: "Division by zero"
**Solution**: Check for missing or zero values in financial data

**Issue**: Excel formula not updating
**Solution**: Ensure Bloomberg Add-in is loaded and you're connected to Terminal

## Support

For questions or issues:
1. Check the main guide: `SECTOR_ANALYSIS_GUIDE.md`
2. Review code comments and docstrings
3. Consult Bloomberg Terminal help: `HELP <GO>`

## Version History

- v1.0 (2024): Initial release
  - Core analysis functions
  - Bloomberg integration guide
  - Excel modeling templates

## License

For personal and educational use.

---

**Ready to start your sector analysis? Begin with `SECTOR_ANALYSIS_GUIDE.md`!**
