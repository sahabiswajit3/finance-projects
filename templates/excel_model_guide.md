# Excel Financial Modeling Guide for Sector Analysis

## Overview
This guide provides templates and best practices for building Excel models for sector analysis.

---

## Excel Workbook Structure

### Recommended Sheet Layout

```
1. Cover & Index
2. Instructions
3. Assumptions
4. Company_List
5. Income_Statement
6. Balance_Sheet
7. Cash_Flow
8. Ratios
9. Valuation
10. Peer_Comparison
11. Historical_Performance
12. Forecasts
13. DCF_Model
14. Scenario_Analysis
15. Dashboard
16. Charts
17. Data_Validation
```

---

## 1. Cover & Index Sheet

**Contents**:
- Report title and sector name
- Analyst name and date
- Version control
- Table of contents with hyperlinks
- Executive summary key findings

---

## 2. Instructions Sheet

**Contents**:
- How to use the model
- Color coding legend
  - **Blue cells**: User inputs
  - **Green cells**: Formulas/calculations
  - **Yellow cells**: Links to other sheets
  - **Orange cells**: Important assumptions
- Navigation guide
- Data update procedures
- Error checking guidance

---

## 3. Assumptions Sheet

**Key Assumptions to Include**:

### Macro Assumptions
- GDP Growth Rate: ____%
- Inflation Rate: ____%
- Interest Rates (10Y Treasury): ____%
- Currency Exchange Rates

### Sector-Specific Assumptions
- Industry Growth Rate: ____%
- Market Size (TAM): $____
- Average Selling Price changes: ____%

### Company-Specific Assumptions
- Revenue Growth Rate (next 5 years)
- EBITDA Margin targets
- CapEx as % of Revenue
- Tax Rate
- Working Capital assumptions

### Valuation Assumptions
- Risk-Free Rate: ____%
- Market Risk Premium: ____%
- WACC components
- Terminal Growth Rate: ____%
- P/E Multiple range

---

## 4. Company List Sheet

**Columns**:
| Ticker | Company Name | Sub-Sector | Market Cap | Country | Currency | Fiscal Year End |
|--------|--------------|------------|------------|---------|----------|-----------------|

**Additional Info**:
- IPO Date
- Index Membership (S&P 500, etc.)
- Analyst Coverage
- Notes

---

## 5. Income Statement Sheet

**Structure**: Years as columns, line items as rows

```
                    2019      2020      2021      2022      2023
Revenue             ___       ___       ___       ___       ___
Cost of Revenue     ___       ___       ___       ___       ___
Gross Profit        ___       ___       ___       ___       ___
                    
Operating Expenses:
  R&D               ___       ___       ___       ___       ___
  SG&A              ___       ___       ___       ___       ___
  Other             ___       ___       ___       ___       ___
Total OpEx          ___       ___       ___       ___       ___

Operating Income    ___       ___       ___       ___       ___
Interest Expense    ___       ___       ___       ___       ___
Other Income        ___       ___       ___       ___       ___
Pre-Tax Income      ___       ___       ___       ___       ___
Tax                 ___       ___       ___       ___       ___
Net Income          ___       ___       ___       ___       ___

EBITDA              ___       ___       ___       ___       ___
EPS                 ___       ___       ___       ___       ___
Shares Outstanding  ___       ___       ___       ___       ___
```

**Key Formulas**:
```excel
Gross Profit = Revenue - Cost of Revenue
Operating Income = Gross Profit - Total Operating Expenses
EPS = Net Income / Shares Outstanding
EBITDA = Operating Income + Depreciation + Amortization
```

---

## 6. Balance Sheet Sheet

**Structure**:
```
Assets              2019      2020      2021      2022      2023
Current Assets:
  Cash              ___       ___       ___       ___       ___
  Accounts Rec      ___       ___       ___       ___       ___
  Inventory         ___       ___       ___       ___       ___
  Other Current     ___       ___       ___       ___       ___
Total Current       ___       ___       ___       ___       ___

Non-Current Assets:
  PP&E              ___       ___       ___       ___       ___
  Intangibles       ___       ___       ___       ___       ___
  Goodwill          ___       ___       ___       ___       ___
  Other             ___       ___       ___       ___       ___
Total Non-Current   ___       ___       ___       ___       ___

TOTAL ASSETS        ___       ___       ___       ___       ___

Liabilities
Current Liab:
  Accounts Payable  ___       ___       ___       ___       ___
  Short-term Debt   ___       ___       ___       ___       ___
  Other Current     ___       ___       ___       ___       ___
Total Current Liab  ___       ___       ___       ___       ___

Non-Current Liab:
  Long-term Debt    ___       ___       ___       ___       ___
  Other             ___       ___       ___       ___       ___
Total Non-Current   ___       ___       ___       ___       ___

Total Liabilities   ___       ___       ___       ___       ___

Shareholders' Equity
  Common Stock      ___       ___       ___       ___       ___
  Retained Earnings ___       ___       ___       ___       ___
  Other             ___       ___       ___       ___       ___
Total Equity        ___       ___       ___       ___       ___

TOTAL LIAB + EQ     ___       ___       ___       ___       ___
```

**Balance Check**:
```excel
=IF(Total_Assets=Total_Liabilities+Total_Equity,"Balanced","ERROR")
```

---

## 7. Cash Flow Sheet

**Structure**:
```
                            2019      2020      2021      2022      2023
Operating Activities:
Net Income                  ___       ___       ___       ___       ___
Adjustments:
  Depreciation              ___       ___       ___       ___       ___
  Changes in WC             ___       ___       ___       ___       ___
  Other                     ___       ___       ___       ___       ___
Cash from Operations        ___       ___       ___       ___       ___

Investing Activities:
  CapEx                     ___       ___       ___       ___       ___
  Acquisitions              ___       ___       ___       ___       ___
  Other                     ___       ___       ___       ___       ___
Cash from Investing         ___       ___       ___       ___       ___

Financing Activities:
  Debt Issued/(Repaid)      ___       ___       ___       ___       ___
  Dividends Paid            ___       ___       ___       ___       ___
  Share Buybacks            ___       ___       ___       ___       ___
  Other                     ___       ___       ___       ___       ___
Cash from Financing         ___       ___       ___       ___       ___

Net Change in Cash          ___       ___       ___       ___       ___
Beginning Cash              ___       ___       ___       ___       ___
Ending Cash                 ___       ___       ___       ___       ___
```

**Free Cash Flow**:
```excel
Free Cash Flow = Cash from Operations - CapEx
```

---

## 8. Ratios Sheet

**Categories and Formulas**:

### Profitability Ratios
```excel
Gross Margin (%) = Gross Profit / Revenue * 100
Operating Margin (%) = Operating Income / Revenue * 100
Net Margin (%) = Net Income / Revenue * 100
EBITDA Margin (%) = EBITDA / Revenue * 100
ROE (%) = Net Income / Shareholders' Equity * 100
ROA (%) = Net Income / Total Assets * 100
ROIC (%) = NOPAT / Invested Capital * 100
```

### Liquidity Ratios
```excel
Current Ratio = Current Assets / Current Liabilities
Quick Ratio = (Current Assets - Inventory) / Current Liabilities
Cash Ratio = Cash / Current Liabilities
```

### Leverage Ratios
```excel
Debt to Equity = Total Debt / Total Equity
Debt to Assets = Total Debt / Total Assets
Interest Coverage = EBIT / Interest Expense
Debt to EBITDA = Total Debt / EBITDA
```

### Efficiency Ratios
```excel
Asset Turnover = Revenue / Average Total Assets
Inventory Turnover = COGS / Average Inventory
Receivables Turnover = Revenue / Average Receivables
Days Sales Outstanding = 365 / Receivables Turnover
```

---

## 9. Valuation Sheet

**Valuation Multiples**:

```
                        Company A  Company B  Company C  Sector Avg
P/E Ratio               ___        ___        ___        ___
P/B Ratio               ___        ___        ___        ___
P/S Ratio               ___        ___        ___        ___
EV/EBITDA               ___        ___        ___        ___
EV/Sales                ___        ___        ___        ___
PEG Ratio               ___        ___        ___        ___
Dividend Yield (%)      ___        ___        ___        ___
```

**Implied Valuation**:
```excel
Implied Price = Sector Average P/E × Company EPS
Upside/Downside (%) = (Implied Price - Current Price) / Current Price * 100
```

---

## 10. Peer Comparison Sheet

**Format**: Side-by-side comparison of key metrics

```
Metric              Co A    Co B    Co C    Co D    Co E    Median    Average
Market Cap (B)      ___     ___     ___     ___     ___     ___       ___
Revenue (M)         ___     ___     ___     ___     ___     ___       ___
Revenue Growth (%)  ___     ___     ___     ___     ___     ___       ___
Gross Margin (%)    ___     ___     ___     ___     ___     ___       ___
EBITDA Margin (%)   ___     ___     ___     ___     ___     ___       ___
Net Margin (%)      ___     ___     ___     ___     ___     ___       ___
ROE (%)             ___     ___     ___     ___     ___     ___       ___
P/E Ratio           ___     ___     ___     ___     ___     ___       ___
EV/EBITDA           ___     ___     ___     ___     ___     ___       ___
Debt/Equity         ___     ___     ___     ___     ___     ___       ___
```

**Conditional Formatting**: Use color scales to highlight best/worst performers

---

## 11. Forecasts Sheet

**5-Year Projection Template**:

```
                    2024E   2025E   2026E   2027E   2028E
Revenue             ___     ___     ___     ___     ___
  YoY Growth (%)    ___     ___     ___     ___     ___
Gross Profit        ___     ___     ___     ___     ___
  Margin (%)        ___     ___     ___     ___     ___
EBITDA              ___     ___     ___     ___     ___
  Margin (%)        ___     ___     ___     ___     ___
Operating Income    ___     ___     ___     ___     ___
Net Income          ___     ___     ___     ___     ___
EPS                 ___     ___     ___     ___     ___
```

**Link assumptions from Assumptions sheet**

---

## 12. DCF Model Sheet

**Template**:

```
WACC Calculation:
Risk-Free Rate                  ____%
Beta                            ___
Market Risk Premium             ____%
Cost of Equity (CAPM)           ____%
Market Value of Equity          $___
Cost of Debt (after-tax)        ____%
Market Value of Debt            $___
WACC                            ____%

Free Cash Flow Forecast:
                    2024E   2025E   2026E   2027E   2028E
EBIT                ___     ___     ___     ___     ___
Tax                 ___     ___     ___     ___     ___
NOPAT               ___     ___     ___     ___     ___
+ D&A               ___     ___     ___     ___     ___
- CapEx             ___     ___     ___     ___     ___
- Chg in WC         ___     ___     ___     ___     ___
Free Cash Flow      ___     ___     ___     ___     ___

Discount Factor     ___     ___     ___     ___     ___
PV of FCF           ___     ___     ___     ___     ___

Terminal Value Calculation:
Terminal Growth Rate            ____%
Terminal Year FCF               $___
Terminal Value                  $___
PV of Terminal Value            $___

Valuation Summary:
Sum of PV of FCF                $___
PV of Terminal Value            $___
Enterprise Value                $___
Less: Net Debt                  $___
Equity Value                    $___
Shares Outstanding              ___
Fair Value per Share            $___
Current Price                   $___
Upside/(Downside)               ___%
```

---

## 13. Scenario Analysis Sheet

**Bull / Base / Bear Cases**:

```
Assumption              Bear    Base    Bull
Revenue Growth (%)      ___     ___     ___
EBITDA Margin (%)       ___     ___     ___
Terminal Growth (%)     ___     ___     ___
WACC (%)                ___     ___     ___

Results:
Fair Value per Share    $___    $___    $___
Upside/(Downside) %     ___%    ___%    ___%
```

**Sensitivity Table**:
- Use Data Table feature (Data → What-If Analysis → Data Table)
- Vary WACC and Terminal Growth Rate
- Show impact on fair value

---

## 14. Dashboard Sheet

**Key Metrics to Display**:

1. **Sector Summary**
   - Total market cap
   - Number of companies
   - Average P/E, P/B
   - Sector growth rate

2. **Top Performers**
   - By revenue growth
   - By margin
   - By return

3. **Key Charts**
   - Revenue trend
   - Margin trend
   - Valuation comparison
   - Market share pie chart

4. **Investment Recommendations**
   - Top picks (Buy)
   - Hold recommendations
   - Avoid (Sell)

---

## Best Practices

### 1. Formatting
- Use consistent fonts (Arial or Calibri, 10-11pt)
- Freeze panes for headers
- Use borders to separate sections
- Apply number formatting consistently
- Use thousands separator for large numbers

### 2. Formulas
- Avoid hardcoding numbers in formulas
- Use named ranges for key inputs
- Add comments to complex formulas
- Use absolute references ($) appropriately
- Avoid circular references

### 3. Data Validation
- Use data validation for inputs
- Create dropdown lists where appropriate
- Set input constraints (min/max values)
- Add input messages and error alerts

### 4. Error Checking
- Use IFERROR() to handle errors gracefully
- Add balance checks
- Create a separate validation sheet
- Use conditional formatting to highlight errors

### 5. Documentation
- Add comments to cells with assumptions
- Create an instructions sheet
- Document data sources
- Note last update date
- Version control

---

## Key Excel Functions for Financial Modeling

### Financial Functions
```excel
=NPV(rate, value1, value2, ...)     - Net Present Value
=IRR(values)                         - Internal Rate of Return
=XNPV(rate, values, dates)          - NPV with specific dates
=XIRR(values, dates)                - IRR with specific dates
=PMT(rate, nper, pv)                - Payment calculation
=FV(rate, nper, pmt, pv)            - Future Value
```

### Lookup Functions
```excel
=VLOOKUP(lookup_value, table, col_index, FALSE)
=HLOOKUP(lookup_value, table, row_index, FALSE)
=INDEX(array, row_num, col_num)
=MATCH(lookup_value, lookup_array, 0)
=INDEX(MATCH())                      - Powerful lookup combo
```

### Statistical Functions
```excel
=AVERAGE(range)                      - Mean
=MEDIAN(range)                       - Median
=STDEV.S(range)                      - Standard deviation
=CORREL(array1, array2)             - Correlation
=SLOPE(known_ys, known_xs)          - Linear regression slope
```

### Conditional Functions
```excel
=IF(condition, true_value, false_value)
=IFERROR(value, value_if_error)
=SUMIF(range, criteria, sum_range)
=COUNTIF(range, criteria)
=AVERAGEIF(range, criteria, average_range)
```

### Array Formulas
```excel
=SUM(array1 * array2)               - Array multiplication
Ctrl+Shift+Enter to confirm array formula
```

---

## Shortcuts

### Essential Excel Shortcuts
- **Ctrl + Arrow**: Navigate to edge of data
- **Ctrl + Shift + Arrow**: Select to edge
- **Ctrl + ;**: Insert today's date
- **Ctrl + '**: Copy formula from above
- **F2**: Edit cell
- **F4**: Toggle absolute/relative references
- **Alt + =**: Auto-sum
- **Ctrl + `**: Show formulas
- **Ctrl + 1**: Format cells dialog
- **Alt + H + O + I**: Auto-fit column width

---

## Quality Checks Before Finalizing

- [ ] All formulas working correctly
- [ ] No #REF!, #VALUE!, #DIV/0! errors
- [ ] Balance sheet balances
- [ ] Cash flow reconciles
- [ ] All assumptions clearly stated
- [ ] Charts properly labeled
- [ ] Consistent formatting throughout
- [ ] Print preview looks good
- [ ] File saved with appropriate name
- [ ] Backup copy created

---

## Additional Resources

### Excel Add-ins
- **Solver**: Optimization problems
- **Analysis ToolPak**: Statistical analysis
- **Power Query**: Data transformation
- **Power Pivot**: Data modeling

### External Tools
- **Bloomberg Excel Add-in**: Live data feeds
- **FactSet**: Financial data
- **Capital IQ**: Company information

---

**Good luck with your Excel modeling!**
