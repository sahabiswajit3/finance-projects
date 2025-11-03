# Sector Analysis Data Collection Checklist

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
