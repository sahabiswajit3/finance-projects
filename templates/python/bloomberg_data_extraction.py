"""
Bloomberg Data Extraction Helper
Script to guide data extraction from Bloomberg Terminal

Author: Finance Projects
Description: Helper functions and templates for extracting data from Bloomberg
"""

# Note: This script provides templates and guidance for Bloomberg data extraction
# Actual Bloomberg API access requires xbbg or pdblp packages and proper authentication

BLOOMBERG_FUNCTIONS = {
    'Company Overview': {
        'Function': 'COMP <TICKER>',
        'Description': 'Complete company overview',
        'Key_Screens': ['Company snapshot', 'Key statistics', 'Executives']
    },
    
    'Financial Analysis': {
        'Function': 'FA <TICKER>',
        'Description': 'Financial statement analysis',
        'Data': ['Income Statement', 'Balance Sheet', 'Cash Flow']
    },
    
    'Relative Valuation': {
        'Function': 'RV <TICKER>',
        'Description': 'Valuation multiples and comparisons',
        'Metrics': ['P/E', 'P/B', 'EV/EBITDA', 'P/S', 'Dividend Yield']
    },
    
    'Industry Analysis': {
        'Function': 'BI <SECTOR>',
        'Description': 'Sector and industry deep dive',
        'Data': ['Industry trends', 'Market size', 'Growth rates']
    }
}


# Bloomberg Field Names for Data Extraction
BLOOMBERG_FIELDS = {
    # Income Statement
    'SALES_REV_TURN': 'Total Revenue',
    'GROSS_PROFIT': 'Gross Profit',
    'EBITDA': 'EBITDA',
    'OPER_INCOME': 'Operating Income',
    'EBIT': 'EBIT',
    'NET_INCOME': 'Net Income',
    'NORMALIZED_NET_INCOME': 'Normalized Net Income',
    'IS_EPS': 'Earnings Per Share',
    
    # Balance Sheet
    'TOTAL_ASSETS': 'Total Assets',
    'TOTAL_LIABILITIES': 'Total Liabilities',
    'TOT_DEBT_TO_TOT_ASSET': 'Total Debt to Total Assets',
    'CASH_AND_MARKETABLE_SECURITIES': 'Cash and Marketable Securities',
    'BS_TOT_DEBT': 'Total Debt',
    'BOOK_VAL_PER_SH': 'Book Value Per Share',
    'WORKING_CAPITAL': 'Working Capital',
    'CURR_RATIO': 'Current Ratio',
    
    # Cash Flow
    'CF_CASH_FROM_OPER': 'Operating Cash Flow',
    'CF_CAP_EXPEND': 'Capital Expenditures',
    'CF_FREE_CASH_FLOW': 'Free Cash Flow',
    'CF_DVD_PAID': 'Dividends Paid',
    
    # Market Data
    'PX_LAST': 'Last Price',
    'PX_TO_BOOK_RATIO': 'Price to Book Ratio',
    'PE_RATIO': 'P/E Ratio',
    'TRAIL_12M_EV_TO_EBITDA': 'EV/EBITDA',
    'CUR_MKT_CAP': 'Market Capitalization',
    'ENTERPRISE_VALUE': 'Enterprise Value',
    'DVD_YIELD': 'Dividend Yield',
    'AVERAGE_VOLUME': 'Average Volume',
    
    # Performance Metrics
    'RETURN_ON_EQUITY': 'Return on Equity',
    'RETURN_ON_ASSETS': 'Return on Assets',
    'RETURN_ON_COMMON_EQUITY': 'Return on Common Equity',
    'RETURN_ON_INV_CAPITAL': 'Return on Invested Capital'
}


def print_bloomberg_guide():
    """Print quick reference guide for Bloomberg Terminal"""
    print("=" * 80)
    print("BLOOMBERG TERMINAL DATA EXTRACTION GUIDE".center(80))
    print("=" * 80)
    print("\n1. ESSENTIAL BLOOMBERG FUNCTIONS\n")
    
    for category, info in BLOOMBERG_FUNCTIONS.items():
        print(f"   {category}:")
        print(f"   Function: {info['Function']}")
        print(f"   Description: {info['Description']}")
        print()
    
    print("\n2. DATA EXTRACTION WORKFLOW\n")
    print("   Step 1: Create company list in PORT function")
    print("   Step 2: Use FMAP to map required fields")
    print("   Step 3: Export using Excel Add-in or API")
    print("   Step 4: Save to data/raw/ directory")
    
    print("\n3. BLOOMBERG EXCEL ADD-IN FORMULAS\n")
    print("   =BDP(ticker, field)          - Single data point")
    print("   =BDH(ticker, field, start, end) - Historical data")
    print("   =BDS(ticker, field)          - Bulk data")
    
    print("\n4. KEY BLOOMBERG COMMANDS\n")
    commands = [
        ("COMP", "Company overview"),
        ("FA", "Financial analysis"),
        ("CF", "Cash flow"),
        ("DVD", "Dividend analysis"),
        ("RV", "Relative valuation"),
        ("PEER", "Peer analysis"),
        ("GP", "Graph prices"),
        ("HRA", "Historical return analysis"),
        ("RELS", "Related securities"),
        ("SECF", "Sector & industry"),
        ("MEMB", "Index members"),
        ("MA", "M&A analysis"),
        ("SPLC", "Supply chain"),
        ("BRC", "Broker research")
    ]
    
    for cmd, desc in commands:
        print(f"   {cmd:<10} - {desc}")
    
    print("\n" + "=" * 80)


def create_field_list(output_file='bloomberg_fields.txt'):
    """Create a text file with Bloomberg fields for easy reference"""
    with open(output_file, 'w') as f:
        f.write("BLOOMBERG FIELD REFERENCE\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("INCOME STATEMENT FIELDS\n")
        f.write("-" * 50 + "\n")
        for field, description in BLOOMBERG_FIELDS.items():
            if any(x in field for x in ['SALES', 'GROSS', 'EBITDA', 'OPER', 'EBIT', 'NET', 'EPS', 'IS_']):
                f.write(f"{field:<35} | {description}\n")
        
        f.write("\n\nBALANCE SHEET FIELDS\n")
        f.write("-" * 50 + "\n")
        for field, description in BLOOMBERG_FIELDS.items():
            if any(x in field for x in ['TOTAL_', 'TOT_', 'BS_', 'BOOK_', 'WORKING', 'CURR_']):
                f.write(f"{field:<35} | {description}\n")
        
        f.write("\n\nCASH FLOW FIELDS\n")
        f.write("-" * 50 + "\n")
        for field, description in BLOOMBERG_FIELDS.items():
            if 'CF_' in field:
                f.write(f"{field:<35} | {description}\n")
        
        f.write("\n\nMARKET DATA FIELDS\n")
        f.write("-" * 50 + "\n")
        for field, description in BLOOMBERG_FIELDS.items():
            if any(x in field for x in ['PX_', 'PE_', 'MKT_', 'ENTERPRISE', 'DVD_', 'VOLUME']):
                f.write(f"{field:<35} | {description}\n")
        
        f.write("\n\nPERFORMANCE METRICS\n")
        f.write("-" * 50 + "\n")
        for field, description in BLOOMBERG_FIELDS.items():
            if 'RETURN_' in field:
                f.write(f"{field:<35} | {description}\n")
    
    print(f"✓ Bloomberg field reference saved to {output_file}")


# Example: Bloomberg Excel formula templates
EXCEL_FORMULA_TEMPLATES = """
BLOOMBERG EXCEL FORMULA TEMPLATES
==================================

1. Current Price:
   =BDP("AAPL US Equity", "PX_LAST")

2. Historical Prices (5 years):
   =BDH("AAPL US Equity", "PX_LAST", TODAY()-1825, TODAY())

3. Financial Data (Revenue):
   =BDP("AAPL US Equity", "SALES_REV_TURN", "BEST_FPERIOD_OVERRIDE=2023")

4. Multiple Fields:
   =BDP("AAPL US Equity", "NET_INCOME|TOTAL_ASSETS|SHAREHOLDERS_EQUITY")

5. Peer Data:
   =BDP("AAPL US Equity", "PEER_TICKER")
   Then use VLOOKUP or BDP for each peer

6. Historical Financials:
   =BDH("AAPL US Equity", "SALES_REV_TURN", "12/31/2018", "12/31/2023", "Per=CY")

7. Multiple Companies (Array Formula):
   Create list of tickers in column A, then:
   =BDP(A2:A20, "PX_LAST|PE_RATIO|DVD_YIELD")

8. Earnings Estimates:
   =BDP("AAPL US Equity", "BEST_EPS_GAAP")

USEFUL OVERRIDES:
- BEST_FPERIOD_OVERRIDE=2023  (Specific fiscal year)
- Per=CY                       (Calendar year)
- Per=FY                       (Fiscal year)
- Per=Q                        (Quarterly)
- Eqy_Fund_Crncy=USD          (Currency conversion)
"""


def generate_data_template(output_file='data_collection_template.md'):
    """Generate a markdown template for data collection checklist"""
    template = """# Sector Analysis Data Collection Checklist

## Phase 1: Company Identification
- [ ] Create list of companies in sector
- [ ] Verify tickers and identifiers
- [ ] Classify by sub-sector/industry
- [ ] Note market cap and listing exchange

## Phase 2: Financial Data (5 Years Annual)
### Income Statement
- [ ] Revenue (SALES_REV_TURN)
- [ ] Gross Profit (GROSS_PROFIT)
- [ ] EBITDA (EBITDA)
- [ ] Operating Income (OPER_INCOME)
- [ ] EBIT (EBIT)
- [ ] Net Income (NET_INCOME)
- [ ] EPS (IS_EPS)

### Balance Sheet
- [ ] Total Assets (TOTAL_ASSETS)
- [ ] Total Liabilities (TOTAL_LIABILITIES)
- [ ] Total Debt (BS_TOT_DEBT)
- [ ] Cash (CASH_AND_MARKETABLE_SECURITIES)
- [ ] Shareholders' Equity (TOT_COMMON_EQY)
- [ ] Working Capital (WORKING_CAPITAL)

### Cash Flow
- [ ] Operating Cash Flow (CF_CASH_FROM_OPER)
- [ ] CapEx (CF_CAP_EXPEND)
- [ ] Free Cash Flow (CF_FREE_CASH_FLOW)
- [ ] Dividends Paid (CF_DVD_PAID)

## Phase 3: Market Data (Current + 5 Years)
- [ ] Current Price (PX_LAST)
- [ ] Historical Prices (BDH)
- [ ] Market Cap (CUR_MKT_CAP)
- [ ] Enterprise Value (ENTERPRISE_VALUE)
- [ ] P/E Ratio (PE_RATIO)
- [ ] P/B Ratio (PX_TO_BOOK_RATIO)
- [ ] EV/EBITDA (TRAIL_12M_EV_TO_EBITDA)
- [ ] Dividend Yield (DVD_YIELD)
- [ ] Beta (BETA_RAW_OVERRIDABLE)
- [ ] 52-Week High/Low

## Phase 4: Performance Metrics
- [ ] ROE (RETURN_ON_EQUITY)
- [ ] ROA (RETURN_ON_ASSETS)
- [ ] ROIC (RETURN_ON_INV_CAPITAL)
- [ ] Gross Margin (GROSS_MARGIN)
- [ ] Operating Margin (OPER_MARGIN)
- [ ] Net Margin (NET_INCOME/SALES_REV_TURN)

## Phase 5: Industry Data
- [ ] Industry classification (GICS)
- [ ] Peer companies (PEER_TICKER)
- [ ] Market share data
- [ ] Industry growth rates
- [ ] Total Addressable Market (TAM)

## Phase 6: Additional Data
- [ ] Analyst estimates (BEST_EPS_GAAP)
- [ ] Credit ratings (RTG_SP, RTG_MOODY, RTG_FITCH)
- [ ] Dividend history (DVD_HIST_ALL)
- [ ] M&A activity
- [ ] Major shareholders (HDS)
- [ ] Supply chain info (SPLC)

## Export Format
- [ ] Save raw data to data/raw/
- [ ] Name files with date: sector_financials_YYYYMMDD.xlsx
- [ ] Keep backup copies
- [ ] Document data sources and dates
- [ ] Note any missing or unusual data points

## Data Quality Checks
- [ ] Verify no missing key fields
- [ ] Check for outliers or anomalies
- [ ] Ensure currency consistency
- [ ] Validate calculations
- [ ] Cross-reference with company filings
"""
    
    with open(output_file, 'w') as f:
        f.write(template)
    
    print(f"✓ Data collection template saved to {output_file}")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("Bloomberg Data Extraction Helper".center(80))
    print("=" * 80 + "\n")
    
    # Print guide
    print_bloomberg_guide()
    
    # Create reference files
    print("\nGenerating reference files...\n")
    create_field_list('templates/bloomberg_fields.txt')
    generate_data_template('templates/data_collection_template.md')
    
    print("\n" + "=" * 80)
    print("Setup Complete!".center(80))
    print("=" * 80)
    print("\nFiles created:")
    print("  - templates/bloomberg_fields.txt")
    print("  - templates/data_collection_template.md")
    print("\nNext steps:")
    print("  1. Review SECTOR_ANALYSIS_GUIDE.md for complete workflow")
    print("  2. Use Bloomberg Terminal to extract data using the field list")
    print("  3. Save exported data to data/raw/")
    print("  4. Run sector_analysis.py to analyze the data")
    print("=" * 80)
