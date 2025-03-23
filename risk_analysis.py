import pandas as pd
import numpy as np

def compute_sharpe_ratio(df, risk_free_rate=0.01):
    # Calculate daily returns if not already present
    if 'returns' not in df.columns:
        df['returns'] = df['price'].pct_change()
    
    # Annualize the metrics (252 trading days)
    annual_return = df['returns'].mean() * 252
    annual_volatility = df['returns'].std() * np.sqrt(252)
    
    # Compute Sharpe Ratio
    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
    
    return sharpe_ratio

def compute_sortino_ratio(df, risk_free_rate=0.01):
    """
    Calculate Sortino Ratio using downside deviation instead of standard deviation
    """
    # Calculate daily returns if not already present
    if 'returns' not in df.columns:
        df['returns'] = df['price'].pct_change()
    
    # Annualize the return
    annual_return = df['returns'].mean() * 252
    
    # Calculate downside returns (only negative returns)
    downside_returns = df['returns'][df['returns'] < 0]
    
    # Calculate downside deviation (annualized)
    downside_std = np.sqrt(252) * np.sqrt(np.mean(downside_returns**2))
    
    # Compute Sortino Ratio
    sortino_ratio = (annual_return - risk_free_rate) / downside_std
    
    return sortino_ratio

def get_risk_metrics(df, risk_free_rate=0.01):
    """
    Calculate both Sharpe and Sortino ratios
    """
    sharpe = compute_sharpe_ratio(df, risk_free_rate)
    sortino = compute_sortino_ratio(df, risk_free_rate)
    
    return {
        'sharpe_ratio': sharpe,
        'sortino_ratio': sortino
    }