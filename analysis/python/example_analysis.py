"""
Example Sector Analysis Script
This script demonstrates how to use the SectorAnalysis toolkit

Usage:
    python example_analysis.py
"""

import sys
sys.path.append('../../templates/python')

from sector_analysis import SectorAnalysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Example workflow for sector analysis
    """
    
    print("=" * 70)
    print("SECTOR ANALYSIS EXAMPLE".center(70))
    print("=" * 70)
    
    # =========================================================================
    # STEP 1: Initialize Analysis
    # =========================================================================
    print("\n1. Initializing Analysis...")
    analysis = SectorAnalysis(data_path='../../data/processed')
    
    # Note: Uncomment below when you have actual data files
    # analysis.load_data(
    #     company_file='company_list.xlsx',
    #     financials_file='financials.xlsx',
    #     prices_file='prices.xlsx'
    # )
    
    # =========================================================================
    # STEP 2: Example - Calculate Financial Ratios
    # =========================================================================
    print("\n2. Calculating Financial Ratios (Example)...")
    
    # Create example financial data
    example_data = pd.DataFrame({
        'Revenue': [1000, 1100, 1210, 1331, 1464],
        'Gross_Profit': [600, 660, 726, 799, 878],
        'Operating_Income': [200, 220, 242, 266, 293],
        'Net_Income': [150, 165, 182, 200, 220],
        'EBITDA': [250, 275, 303, 333, 366],
        'Total_Assets': [2000, 2200, 2420, 2662, 2928],
        'Shareholders_Equity': [1000, 1100, 1210, 1331, 1464],
        'Total_Debt': [500, 520, 541, 563, 586],
        'Current_Assets': [800, 880, 968, 1065, 1171],
        'Current_Liabilities': [400, 420, 441, 463, 486],
        'Inventory': [100, 105, 110, 116, 122],
        'EBIT': [200, 220, 242, 266, 293],
        'Interest_Expense': [20, 21, 22, 23, 24]
    })
    
    ratios = analysis.calculate_ratios(example_data)
    print("\nCalculated Ratios:")
    print(ratios.to_string())
    
    # =========================================================================
    # STEP 3: Example - Calculate Growth Rates
    # =========================================================================
    print("\n3. Calculating Growth Rates (Example)...")
    
    revenue_cagr = analysis.calculate_growth_rates(example_data, 'Revenue', periods=4)
    print(f"   Revenue CAGR (4 years): {revenue_cagr}%")
    
    ebitda_cagr = analysis.calculate_growth_rates(example_data, 'EBITDA', periods=4)
    print(f"   EBITDA CAGR (4 years): {ebitda_cagr}%")
    
    # =========================================================================
    # STEP 4: Example - DCF Valuation
    # =========================================================================
    print("\n4. DCF Valuation (Example)...")
    
    # 5-year Free Cash Flow forecast (in millions)
    fcf_forecast = [100, 110, 121, 133, 146]
    
    # Valuation parameters
    wacc = 0.10              # 10% Weighted Average Cost of Capital
    terminal_growth = 0.02   # 2% Terminal Growth Rate
    net_debt = 500           # $500M Net Debt
    shares = 100             # 100M Shares Outstanding
    
    valuation = analysis.dcf_valuation(
        fcf_forecast=fcf_forecast,
        wacc=wacc,
        terminal_growth=terminal_growth,
        net_debt=net_debt,
        shares=shares
    )
    
    print(f"\n   DCF Valuation Results:")
    print(f"   Enterprise Value: ${valuation['Enterprise_Value']:,.2f}M")
    print(f"   Equity Value: ${valuation['Equity_Value']:,.2f}M")
    print(f"   Fair Value per Share: ${valuation['Price_Per_Share']:.2f}")
    print(f"   PV of Forecast Period: ${valuation['PV_Forecast']:,.2f}M")
    print(f"   PV of Terminal Value: ${valuation['PV_Terminal']:,.2f}M")
    
    # =========================================================================
    # STEP 5: Example - Risk Analysis
    # =========================================================================
    print("\n5. Risk Analysis (Example)...")
    
    # Generate example returns data (252 trading days)
    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 252)  # Mean=0.1%, Std=2%
    
    risk_metrics = analysis.risk_metrics(returns, risk_free_rate=0.02)
    
    print(f"\n   Risk Metrics:")
    print(f"   Mean Annual Return: {risk_metrics['Mean_Annual_Return']}%")
    print(f"   Annual Volatility: {risk_metrics['Annual_Volatility']}%")
    print(f"   Sharpe Ratio: {risk_metrics['Sharpe_Ratio']}")
    print(f"   Max Drawdown: {risk_metrics['Max_Drawdown']}%")
    print(f"   VaR (95%): {risk_metrics['VaR_95']}%")
    print(f"   VaR (99%): {risk_metrics['VaR_99']}%")
    
    # =========================================================================
    # STEP 6: Example - Market Concentration Analysis
    # =========================================================================
    print("\n6. Market Concentration Analysis (Example)...")
    
    # Market shares of top players (in %)
    market_shares = [30, 20, 15, 12, 8, 15]  # Total = 100%
    
    concentration = analysis.market_concentration(market_shares)
    
    print(f"\n   Market Concentration Metrics:")
    print(f"   HHI (Herfindahl-Hirschman Index): {concentration['HHI']}")
    print(f"   CR3 (Top 3 Market Share): {concentration['CR3']}%")
    print(f"   CR5 (Top 5 Market Share): {concentration['CR5']}%")
    print(f"   Interpretation: {concentration['Interpretation']}")
    
    # =========================================================================
    # STEP 7: Example - Scenario Analysis
    # =========================================================================
    print("\n7. Scenario Analysis (Example)...")
    
    base_case = {
        'Revenue_Growth': 10.0,
        'EBITDA_Margin': 30.0,
        'Fair_Value': 50.00
    }
    
    scenarios = {
        'Bull Case': {
            'Revenue_Growth': 15.0,
            'EBITDA_Margin': 35.0,
            'Fair_Value': 65.00
        },
        'Bear Case': {
            'Revenue_Growth': 5.0,
            'EBITDA_Margin': 25.0,
            'Fair_Value': 35.00
        }
    }
    
    scenario_df = analysis.scenario_analysis(base_case, scenarios)
    print("\n   Scenario Comparison:")
    print(scenario_df.to_string())
    
    # =========================================================================
    # STEP 8: Example - Create Visualization
    # =========================================================================
    print("\n8. Creating Visualization (Example)...")
    
    # Create a simple trend chart
    fig = analysis.trend_analysis(
        example_data, 
        'Revenue', 
        window=3,
        title='Revenue Trend Analysis (5 Years)'
    )
    
    # Save the chart
    output_dir = 'output'
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    plt.savefig(f'{output_dir}/revenue_trend.png', dpi=150, bbox_inches='tight')
    print(f"   ✓ Chart saved to {output_dir}/revenue_trend.png")
    plt.close()
    
    # =========================================================================
    # STEP 9: Generate Report
    # =========================================================================
    print("\n9. Generating Summary Report...")
    
    analysis.generate_report(output_path='output')
    
    # =========================================================================
    # COMPLETE
    # =========================================================================
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE!".center(70))
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Review the output files in the 'output/' directory")
    print("2. Customize this script with your actual data")
    print("3. Add sector-specific metrics and analysis")
    print("4. Create additional visualizations")
    print("5. Build comprehensive models and reports")
    print("\nFor complete guidance, see:")
    print("- SECTOR_ANALYSIS_GUIDE.md")
    print("- QUICK_START.md")
    print("- templates/README.md")
    print("=" * 70)


if __name__ == "__main__":
    main()
