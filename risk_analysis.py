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