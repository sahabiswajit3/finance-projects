"""
Sector Analysis Toolkit
A comprehensive Python library for financial sector analysis

Author: Finance Projects
Description: Tools for analyzing sectors, industries, and companies using
             financial data from Bloomberg and other sources.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class SectorAnalysis:
    """
    Comprehensive sector analysis toolkit
    """
    
    def __init__(self, data_path):
        """
        Initialize with path to data directory
        
        Parameters:
        -----------
        data_path : str
            Path to directory containing data files
        """
        self.data_path = data_path
        self.companies_df = None
        self.financials_df = None
        self.prices_df = None
    
    def load_data(self, company_file='company_list.xlsx', 
                  financials_file='financials.xlsx',
                  prices_file='prices.xlsx'):
        """
        Load financial and market data from Excel files
        
        Parameters:
        -----------
        company_file : str
            Filename for company list
        financials_file : str
            Filename for financial data
        prices_file : str
            Filename for price data
        """
        try:
            self.companies_df = pd.read_excel(f'{self.data_path}/{company_file}')
            self.financials_df = pd.read_excel(f'{self.data_path}/{financials_file}')
            self.prices_df = pd.read_excel(f'{self.data_path}/{prices_file}')
            print("✓ Data loaded successfully")
            print(f"  - Companies: {len(self.companies_df)}")
            print(f"  - Financial records: {len(self.financials_df)}")
            print(f"  - Price records: {len(self.prices_df)}")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def calculate_ratios(self, df):
        """
        Calculate comprehensive financial ratios
        
        Parameters:
        -----------
        df : DataFrame
            DataFrame with financial data
            
        Returns:
        --------
        DataFrame with calculated ratios
        """
        ratios = pd.DataFrame(index=df.index)
        
        # Profitability ratios
        if 'Gross_Profit' in df.columns and 'Revenue' in df.columns:
            ratios['Gross_Margin'] = (df['Gross_Profit'] / df['Revenue'] * 100).round(2)
        
        if 'Operating_Income' in df.columns and 'Revenue' in df.columns:
            ratios['Operating_Margin'] = (df['Operating_Income'] / df['Revenue'] * 100).round(2)
        
        if 'Net_Income' in df.columns and 'Revenue' in df.columns:
            ratios['Net_Margin'] = (df['Net_Income'] / df['Revenue'] * 100).round(2)
        
        if 'EBITDA' in df.columns and 'Revenue' in df.columns:
            ratios['EBITDA_Margin'] = (df['EBITDA'] / df['Revenue'] * 100).round(2)
        
        if 'Net_Income' in df.columns and 'Shareholders_Equity' in df.columns:
            ratios['ROE'] = (df['Net_Income'] / df['Shareholders_Equity'] * 100).round(2)
        
        if 'Net_Income' in df.columns and 'Total_Assets' in df.columns:
            ratios['ROA'] = (df['Net_Income'] / df['Total_Assets'] * 100).round(2)
        
        # Leverage ratios
        if 'Total_Debt' in df.columns and 'Shareholders_Equity' in df.columns:
            ratios['Debt_to_Equity'] = (df['Total_Debt'] / df['Shareholders_Equity']).round(2)
        
        if 'Total_Debt' in df.columns and 'Total_Assets' in df.columns:
            ratios['Debt_to_Assets'] = (df['Total_Debt'] / df['Total_Assets']).round(2)
        
        if 'EBIT' in df.columns and 'Interest_Expense' in df.columns:
            ratios['Interest_Coverage'] = (df['EBIT'] / df['Interest_Expense']).round(2)
        
        # Liquidity ratios
        if 'Current_Assets' in df.columns and 'Current_Liabilities' in df.columns:
            ratios['Current_Ratio'] = (df['Current_Assets'] / df['Current_Liabilities']).round(2)
        
        if all(col in df.columns for col in ['Current_Assets', 'Inventory', 'Current_Liabilities']):
            ratios['Quick_Ratio'] = ((df['Current_Assets'] - df['Inventory']) / 
                                      df['Current_Liabilities']).round(2)
        
        return ratios
    
    def calculate_growth_rates(self, df, metric, periods=None):
        """
        Calculate CAGR (Compound Annual Growth Rate) for given metric
        
        Parameters:
        -----------
        df : DataFrame
            DataFrame with time series data
        metric : str
            Name of the metric column
        periods : int, optional
            Number of periods. If None, uses entire series length
            
        Returns:
        --------
        float : CAGR as percentage
        """
        if metric not in df.columns:
            print(f"Warning: {metric} not found in dataframe")
            return None
        
        series = df[metric].dropna()
        if len(series) < 2:
            print("Warning: Insufficient data for growth calculation")
            return None
        
        start_value = series.iloc[0]
        end_value = series.iloc[-1]
        
        if periods is None:
            periods = len(series) - 1
        
        if start_value <= 0:
            print("Warning: Start value must be positive for CAGR calculation")
            return None
        
        cagr = ((end_value / start_value) ** (1/periods) - 1) * 100
        return round(cagr, 2)
    
    def peer_comparison(self, companies, metrics, title='Peer Comparison'):
        """
        Create peer comparison visualization
        
        Parameters:
        -----------
        companies : list
            List of company names
        metrics : list
            List of metrics to compare
        title : str
            Chart title
            
        Returns:
        --------
        matplotlib figure
        """
        n_metrics = min(len(metrics), 4)
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        axes = axes.flatten()
        
        for idx in range(n_metrics):
            metric = metrics[idx]
            ax = axes[idx]
            
            if self.financials_df is not None:
                data = self.financials_df[self.financials_df['Company'].isin(companies)]
                if not data.empty and metric in data.columns:
                    avg_data = data.groupby('Company')[metric].mean()
                    avg_data.plot(kind='bar', ax=ax, color='steelblue')
                    ax.set_title(f'{metric} Comparison', fontsize=12, fontweight='bold')
                    ax.set_ylabel(metric)
                    ax.set_xlabel('')
                    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
                    ax.grid(axis='y', alpha=0.3)
        
        # Hide unused subplots
        for idx in range(n_metrics, 4):
            axes[idx].axis('off')
        
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.00)
        plt.tight_layout()
        return fig
    
    def valuation_analysis(self, df):
        """
        Analyze valuation multiples
        
        Parameters:
        -----------
        df : DataFrame
            DataFrame with price and financial data
            
        Returns:
        --------
        DataFrame with valuation metrics
        """
        valuation = pd.DataFrame(index=df.index)
        
        if 'Price' in df.columns and 'EPS' in df.columns:
            valuation['PE_Ratio'] = (df['Price'] / df['EPS']).round(2)
        
        if 'Price' in df.columns and 'Book_Value_Per_Share' in df.columns:
            valuation['PB_Ratio'] = (df['Price'] / df['Book_Value_Per_Share']).round(2)
        
        if 'Market_Cap' in df.columns and 'Revenue' in df.columns:
            valuation['PS_Ratio'] = (df['Market_Cap'] / df['Revenue']).round(2)
        
        if 'Enterprise_Value' in df.columns and 'EBITDA' in df.columns:
            valuation['EV_EBITDA'] = (df['Enterprise_Value'] / df['EBITDA']).round(2)
        
        if 'Enterprise_Value' in df.columns and 'Revenue' in df.columns:
            valuation['EV_Sales'] = (df['Enterprise_Value'] / df['Revenue']).round(2)
        
        return valuation
    
    def trend_analysis(self, df, metric, window=4, title=None):
        """
        Analyze trends with moving average
        
        Parameters:
        -----------
        df : DataFrame
            DataFrame with time series data
        metric : str
            Name of metric to analyze
        window : int
            Window size for moving average
        title : str, optional
            Chart title
            
        Returns:
        --------
        matplotlib figure
        """
        if metric not in df.columns:
            print(f"Error: {metric} not found in dataframe")
            return None
        
        data = df[metric].dropna()
        ma = data.rolling(window=window).mean()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data.index, data.values, label=metric, marker='o', linewidth=2)
        ax.plot(ma.index, ma.values, label=f'{window}-Period MA', 
                linestyle='--', linewidth=2)
        
        title = title or f'{metric} Trend Analysis'
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Period', fontsize=11)
        ax.set_ylabel(metric, fontsize=11)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return fig
    
    def correlation_matrix(self, df, title='Correlation Matrix'):
        """
        Create correlation matrix visualization
        
        Parameters:
        -----------
        df : DataFrame
            DataFrame with numeric columns
        title : str
            Chart title
            
        Returns:
        --------
        matplotlib figure
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                    center=0, square=True, linewidths=1, 
                    cbar_kws={"shrink": 0.8}, ax=ax)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        
        return fig
    
    def dcf_valuation(self, fcf_forecast, wacc, terminal_growth, net_debt, shares):
        """
        Discounted Cash Flow (DCF) valuation
        
        Parameters:
        -----------
        fcf_forecast : list or array
            Forecasted free cash flows
        wacc : float
            Weighted Average Cost of Capital (decimal, e.g., 0.10 for 10%)
        terminal_growth : float
            Perpetual growth rate (decimal, e.g., 0.02 for 2%)
        net_debt : float
            Net debt amount
        shares : float
            Shares outstanding
            
        Returns:
        --------
        dict with valuation components
        """
        # Present value of forecast period
        pv_fcf = sum([fcf / (1 + wacc)**i for i, fcf in enumerate(fcf_forecast, 1)])
        
        # Terminal value
        terminal_fcf = fcf_forecast[-1] * (1 + terminal_growth)
        terminal_value = terminal_fcf / (wacc - terminal_growth)
        pv_terminal = terminal_value / (1 + wacc)**len(fcf_forecast)
        
        # Enterprise and equity value
        enterprise_value = pv_fcf + pv_terminal
        equity_value = enterprise_value - net_debt
        price_per_share = equity_value / shares
        
        results = {
            'Enterprise_Value': round(enterprise_value, 2),
            'Equity_Value': round(equity_value, 2),
            'Price_Per_Share': round(price_per_share, 2),
            'PV_Forecast': round(pv_fcf, 2),
            'PV_Terminal': round(pv_terminal, 2),
            'Terminal_Value': round(terminal_value, 2)
        }
        
        return results
    
    def monte_carlo_simulation(self, base_value, volatility, drift, 
                              periods=252, simulations=10000):
        """
        Monte Carlo simulation for price projection
        
        Parameters:
        -----------
        base_value : float
            Starting value
        volatility : float
            Annual volatility (decimal)
        drift : float
            Expected annual return (decimal)
        periods : int
            Number of periods (252 for trading days in a year)
        simulations : int
            Number of simulation paths
            
        Returns:
        --------
        numpy array of price paths
        """
        dt = 1/periods
        price_paths = np.zeros((periods, simulations))
        price_paths[0] = base_value
        
        for t in range(1, periods):
            random_shock = np.random.standard_normal(simulations)
            price_paths[t] = price_paths[t-1] * np.exp(
                (drift - 0.5*volatility**2)*dt + 
                volatility*np.sqrt(dt)*random_shock
            )
        
        return price_paths
    
    def risk_metrics(self, returns, risk_free_rate=0.02):
        """
        Calculate comprehensive risk metrics
        
        Parameters:
        -----------
        returns : array-like
            Series of returns
        risk_free_rate : float
            Risk-free rate (decimal, annualized)
            
        Returns:
        --------
        dict with risk metrics
        """
        returns = np.array(returns)
        
        # Annualized metrics (assuming daily returns)
        mean_return = returns.mean() * 252
        volatility = returns.std() * np.sqrt(252)
        
        # Sharpe ratio
        sharpe = (mean_return - risk_free_rate) / volatility if volatility > 0 else 0
        
        # Maximum drawdown
        cumulative = (1 + returns).cumprod()
        running_max = np.maximum.accumulate(cumulative)
        drawdown = (cumulative - running_max) / running_max
        max_drawdown = drawdown.min()
        
        # Value at Risk
        var_95 = np.percentile(returns, 5)
        var_99 = np.percentile(returns, 1)
        
        # Conditional VaR (CVaR / Expected Shortfall)
        cvar_95 = returns[returns <= var_95].mean()
        cvar_99 = returns[returns <= var_99].mean()
        
        metrics = {
            'Mean_Annual_Return': round(mean_return * 100, 2),
            'Annual_Volatility': round(volatility * 100, 2),
            'Sharpe_Ratio': round(sharpe, 3),
            'Max_Drawdown': round(max_drawdown * 100, 2),
            'VaR_95': round(var_95 * 100, 2),
            'VaR_99': round(var_99 * 100, 2),
            'CVaR_95': round(cvar_95 * 100, 2),
            'CVaR_99': round(cvar_99 * 100, 2)
        }
        
        return metrics
    
    def market_concentration(self, market_shares):
        """
        Calculate market concentration metrics
        
        Parameters:
        -----------
        market_shares : list or array
            Market shares as percentages
            
        Returns:
        --------
        dict with concentration metrics
        """
        shares = np.array(market_shares)
        
        # Herfindahl-Hirschman Index (HHI)
        hhi = np.sum(shares ** 2)
        
        # Concentration ratios
        sorted_shares = np.sort(shares)[::-1]
        cr3 = sorted_shares[:3].sum() if len(sorted_shares) >= 3 else sorted_shares.sum()
        cr5 = sorted_shares[:5].sum() if len(sorted_shares) >= 5 else sorted_shares.sum()
        
        # Interpretation
        if hhi < 1500:
            concentration = "Low (Competitive)"
        elif hhi < 2500:
            concentration = "Moderate"
        else:
            concentration = "High (Concentrated)"
        
        metrics = {
            'HHI': round(hhi, 2),
            'CR3': round(cr3, 2),
            'CR5': round(cr5, 2),
            'Interpretation': concentration
        }
        
        return metrics
    
    def scenario_analysis(self, base_case, scenarios):
        """
        Perform scenario analysis
        
        Parameters:
        -----------
        base_case : dict
            Base case assumptions
        scenarios : dict
            Dictionary of scenarios with assumptions
            
        Returns:
        --------
        DataFrame with scenario results
        """
        results = {'Base Case': base_case}
        results.update(scenarios)
        
        df = pd.DataFrame(results).T
        return df
    
    def generate_report(self, output_path='./reports'):
        """
        Generate summary report
        
        Parameters:
        -----------
        output_path : str
            Path to save the report
        """
        report = []
        report.append("="*70)
        report.append("SECTOR ANALYSIS REPORT".center(70))
        report.append("="*70)
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Data summary
        if self.companies_df is not None:
            report.append(f"Number of Companies Analyzed: {len(self.companies_df)}")
        
        if self.financials_df is not None:
            report.append(f"Financial Records: {len(self.financials_df)}")
        
        if self.prices_df is not None:
            report.append(f"Price Records: {len(self.prices_df)}")
        
        report.append("\n" + "="*70)
        report.append("End of Report".center(70))
        report.append("="*70)
        
        # Save report
        import os
        os.makedirs(output_path, exist_ok=True)
        report_file = f'{output_path}/analysis_summary_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        
        with open(report_file, 'w') as f:
            f.write('\n'.join(report))
        
        print(f"✓ Report saved to {report_file}")


# Example usage
if __name__ == "__main__":
    print("Sector Analysis Toolkit")
    print("=" * 50)
    print("\nExample Usage:\n")
    
    print("# Initialize analysis")
    print("analysis = SectorAnalysis(data_path='./data/processed')")
    print("\n# Load data")
    print("analysis.load_data()")
    print("\n# Calculate ratios")
    print("ratios = analysis.calculate_ratios(analysis.financials_df)")
    print("\n# Calculate growth rates")
    print("growth = analysis.calculate_growth_rates(analysis.financials_df, 'Revenue', periods=5)")
    print("\n# DCF Valuation")
    print("fcf = [100, 110, 121, 133, 146]  # 5-year FCF forecast")
    print("valuation = analysis.dcf_valuation(fcf, wacc=0.10, terminal_growth=0.02,")
    print("                                     net_debt=500, shares=100)")
    print("\n# Generate report")
    print("analysis.generate_report(output_path='./reports')")
