import pandas as pd

def compute_sharpe_ratio(df, risk_free_rate=0.01):
    return (df['returns'].mean() - risk_free_rate / 252) / df['returns'].std()