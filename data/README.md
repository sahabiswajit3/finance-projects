# Data Directory

This directory stores all data for your sector analysis.

## Structure

### `/raw`
Store raw, unmodified data files exported from Bloomberg Terminal or other sources.

**Naming Convention**: `sector_datatype_YYYYMMDD.xlsx`

Examples:
- `technology_financials_20240301.xlsx`
- `healthcare_prices_20240301.xlsx`
- `financials_market_data_20240301.xlsx`

**Best Practices**:
- Never modify files in this directory
- Keep original exports as backup
- Document data source and extraction date
- Store Bloomberg terminal screenshots if helpful

### `/processed`
Store cleaned and processed data ready for analysis.

**Files to create**:
- `company_list.xlsx`: Master list of companies with metadata
- `financials.xlsx`: Combined financial statements (IS, BS, CF)
- `prices.xlsx`: Historical price and return data
- `ratios.xlsx`: Calculated financial ratios
- `market_data.xlsx`: Market cap, valuation multiples, etc.

**Processing Steps**:
1. Import raw data
2. Handle missing values
3. Standardize formats (dates, currencies)
4. Validate data quality
5. Combine multiple sources
6. Save to processed directory

### `/external`
Store data from sources other than Bloomberg.

**Potential Sources**:
- Industry association reports
- Government statistical data
- Company investor relations (10-K, 10-Q)
- Market research firms (Gartner, IDC)
- Academic databases
- News and media sources

## Data Quality Checklist

Before analysis, verify:
- [ ] All required companies have data
- [ ] No missing critical fields
- [ ] Dates are consistent and correct
- [ ] Currency is standardized
- [ ] Outliers are investigated
- [ ] Data matches company filings
- [ ] Source and extraction date documented

## Data Privacy & Security

⚠️ **Important Notes**:
- Bloomberg data may have usage restrictions
- Company data may be proprietary
- Do not share sensitive financial data publicly
- Check licensing before distribution
- This `.gitignore` excludes data files from version control

## File Formats

**Recommended**: Excel (.xlsx) or CSV (.csv)

**Excel Benefits**:
- Multiple sheets per file
- Preserve formatting
- Bloomberg formulas work
- Easy to review

**CSV Benefits**:
- Smaller file size
- Universal compatibility
- Easy to import into Python/R
- Version control friendly

## Example Data Files

See `templates/data_collection_template.md` for complete data requirements.

### Minimum Required Data

#### company_list.xlsx
| Ticker | Company_Name | Sub_Sector | Market_Cap | Country | Currency |
|--------|--------------|------------|------------|---------|----------|

#### financials.xlsx
| Company | Year | Revenue | EBITDA | Net_Income | Total_Assets | Total_Debt |
|---------|------|---------|--------|------------|--------------|------------|

#### prices.xlsx
| Date | Ticker | Price | Volume | Market_Cap |
|------|--------|-------|--------|------------|

## Data Update Schedule

**Recommended**:
- **Quarterly**: After earnings season
- **Annual**: After fiscal year end
- **Ad-hoc**: For major events (M&A, restructuring)

Keep a log of updates:
```
2024-03-01: Initial data collection (5 years historical)
2024-06-01: Q1 2024 update
2024-09-01: Q2 2024 update
```

## Troubleshooting

**Issue**: Missing data points
- Check company reporting calendar
- Verify ticker symbol
- Look for restatements or adjustments

**Issue**: Inconsistent data
- Check for stock splits, dividends
- Verify currency conversion
- Look for one-time items

**Issue**: Large file sizes
- Split by year or company
- Use CSV instead of Excel
- Compress old data

---

**Ready to collect data? Use the checklist in `templates/data_collection_template.md`**
