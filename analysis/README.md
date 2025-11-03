# Analysis Directory

This directory contains your actual analysis work - Python scripts and Excel models.

## Structure

### `/python`
Your Python analysis scripts and notebooks.

**Suggested Files**:
- `01_data_preparation.py`: Load and clean data
- `02_exploratory_analysis.py`: Initial data exploration
- `03_financial_ratios.py`: Calculate and analyze ratios
- `04_peer_comparison.py`: Compare companies
- `05_valuation.py`: DCF and valuation models
- `06_risk_analysis.py`: Risk metrics and stress tests
- `07_visualizations.py`: Create charts and dashboards
- `08_generate_report.py`: Compile final report

### `/excel`
Your Excel financial models and workbooks.

**Suggested Files**:
- `sector_financial_model.xlsx`: Main three-statement model
- `dcf_valuation.xlsx`: DCF valuation models
- `peer_comparison.xlsx`: Peer benchmarking
- `scenario_analysis.xlsx`: Bull/Base/Bear scenarios
- `dashboard.xlsx`: Summary dashboard with charts

## Getting Started with Python

### 1. Import the Toolkit
```python
import sys
sys.path.append('../templates/python')
from sector_analysis import SectorAnalysis

# Initialize
analysis = SectorAnalysis(data_path='../data/processed')
```

### 2. Load Your Data
```python
# Load data
analysis.load_data(
    company_file='company_list.xlsx',
    financials_file='financials.xlsx',
    prices_file='prices.xlsx'
)
```

### 3. Run Analysis
```python
# Calculate ratios
ratios = analysis.calculate_ratios(analysis.financials_df)

# Growth analysis
revenue_growth = analysis.calculate_growth_rates(
    analysis.financials_df, 
    'Revenue', 
    periods=5
)

# Peer comparison
companies = ['Company A', 'Company B', 'Company C']
metrics = ['Revenue', 'EBITDA_Margin', 'ROE', 'PE_Ratio']
fig = analysis.peer_comparison(companies, metrics)
fig.savefig('peer_comparison.png')
```

### 4. Valuation
```python
# DCF Valuation
fcf = [100, 110, 121, 133, 146]  # 5-year forecast
valuation = analysis.dcf_valuation(
    fcf_forecast=fcf,
    wacc=0.10,
    terminal_growth=0.02,
    net_debt=500,
    shares=100
)
print(f"Fair Value: ${valuation['Price_Per_Share']:.2f}")
```

## Python Workflow Example

### Complete Analysis Script

```python
"""
Technology Sector Analysis
Date: 2024-03-01
"""

import sys
sys.path.append('../templates/python')
from sector_analysis import SectorAnalysis
import pandas as pd
import matplotlib.pyplot as plt

# Initialize
print("Initializing analysis...")
analysis = SectorAnalysis(data_path='../data/processed')
analysis.load_data()

# 1. Financial Ratios
print("\n1. Calculating financial ratios...")
ratios = analysis.calculate_ratios(analysis.financials_df)
ratios.to_excel('output/financial_ratios.xlsx')

# 2. Growth Analysis
print("2. Analyzing growth trends...")
growth_metrics = {}
for metric in ['Revenue', 'EBITDA', 'Net_Income']:
    growth = analysis.calculate_growth_rates(
        analysis.financials_df, 
        metric, 
        periods=5
    )
    growth_metrics[metric] = growth

# 3. Peer Comparison
print("3. Creating peer comparisons...")
top_companies = analysis.companies_df.nlargest(5, 'Market_Cap')['Company'].tolist()
fig = analysis.peer_comparison(
    companies=top_companies,
    metrics=['Revenue', 'EBITDA_Margin', 'ROE', 'Debt_to_Equity']
)
fig.savefig('output/peer_comparison.png')

# 4. Valuation
print("4. Running valuation analysis...")
valuations = {}
for company in top_companies:
    # Your DCF logic here
    pass

# 5. Risk Analysis
print("5. Calculating risk metrics...")
for ticker in top_companies:
    prices = analysis.prices_df[analysis.prices_df['Ticker'] == ticker]
    returns = prices['Price'].pct_change().dropna()
    risk = analysis.risk_metrics(returns.values)
    print(f"{ticker}: Sharpe Ratio = {risk['Sharpe_Ratio']:.2f}")

# 6. Generate Report
print("6. Generating report...")
analysis.generate_report(output_path='../reports')

print("\nAnalysis complete!")
```

## Excel Workflow

### 1. Set Up Workbook
- Use structure from `templates/excel_model_guide.md`
- Create all required sheets
- Set up color coding (Blue=inputs, Green=formulas)

### 2. Import Data
- Link to Bloomberg using BDP/BDH functions, OR
- Import CSV/Excel files from `data/processed/`

### 3. Build Models
- Income Statement → Balance Sheet → Cash Flow
- Calculate ratios and metrics
- Build DCF valuation
- Create scenario analysis

### 4. Visualizations
- Revenue and earnings trends
- Margin comparisons
- Valuation multiples
- Market share charts

### 5. Dashboard
- Summary metrics
- Key charts
- Investment recommendations

## Best Practices

### Python
1. **Organize by workflow stage**: Number your scripts (01_, 02_, etc.)
2. **Use functions**: Avoid duplicating code
3. **Comment your code**: Explain complex logic
4. **Save outputs**: Save figures and tables to `output/` subdirectory
5. **Version control**: Commit working versions regularly

### Excel
1. **Separate inputs from calculations**: Blue cells for inputs
2. **Document assumptions**: Add comments and notes
3. **Include checks**: Balance checks, error flags
4. **Use named ranges**: Makes formulas easier to read
5. **Backup regularly**: Save versions with dates

### General
1. **Start simple**: Get basic analysis working first
2. **Iterate**: Refine models based on insights
3. **Validate**: Cross-check results with company filings
4. **Document**: Keep notes on methodology and findings
5. **Review**: Have someone else check your work

## Output Organization

Create an `output/` subdirectory for analysis results:

```
analysis/python/output/
├── charts/
│   ├── peer_comparison.png
│   ├── revenue_trends.png
│   └── valuation_scatter.png
├── tables/
│   ├── financial_ratios.xlsx
│   ├── growth_rates.xlsx
│   └── risk_metrics.xlsx
└── reports/
    └── analysis_summary.txt
```

## Troubleshooting

### Python Issues

**Error**: "ModuleNotFoundError: No module named 'pandas'"
```bash
pip install -r ../../requirements.txt
```

**Error**: "FileNotFoundError: data file not found"
- Check file path is correct
- Ensure data files exist in `data/processed/`

**Error**: "KeyError: column not found"
- Check column names in your data files
- Update column references in code

### Excel Issues

**Issue**: Bloomberg formulas not working
- Ensure Bloomberg Add-in is loaded
- Check Bloomberg Terminal is running
- Verify ticker format (e.g., "AAPL US Equity")

**Issue**: Circular reference error
- Check for formulas that reference themselves
- Use iterative calculation if intentional

**Issue**: #DIV/0! errors
- Add error handling: `=IFERROR(formula, 0)`
- Check for zero or missing values

## Resources

### Python Learning
- Official docs: https://pandas.pydata.org/docs/
- Tutorials: Real Python, DataCamp
- Financial modeling: QuantLib, PyPortfolioOpt

### Excel Learning
- Excel functions: support.microsoft.com
- Financial modeling: Breaking Into Wall Street
- Bloomberg: `HELP <GO>` on Terminal

### Finance
- CFA Institute: industry analysis frameworks
- Damodaran Online: valuation resources
- SEC EDGAR: company filings

---

**Ready to analyze? Start with the template scripts in `templates/python/`**
