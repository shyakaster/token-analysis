import pandas as pd
import matplotlib.pyplot as plt

def compute_volatility(df, window=20):
    return df['returns'].rolling(window=window).std()

def plot_volatility(volatility, token_name):
    plt.figure(figsize=(12, 6))
    plt.plot(volatility, label=f'{token_name} 20-Day Rolling Volatility', color='purple')
    plt.title(f'{token_name} Rolling Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.grid()
    plt.show()