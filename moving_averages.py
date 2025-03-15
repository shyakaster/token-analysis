import pandas as pd
import matplotlib.pyplot as plt

def compute_moving_averages(df):
    df['SMA_20'] = df['price'].rolling(window=20).mean()
    df['SMA_50'] = df['price'].rolling(window=50).mean()
    return df

def plot_moving_averages(df, token_name):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label=f'{token_name} Price', color='blue')
    plt.plot(df.index, df['SMA_20'], label='20-Day SMA', color='red', linestyle='dashed')
    plt.plot(df.index, df['SMA_50'], label='50-Day SMA', color='green', linestyle='dashed')
    plt.title(f'{token_name} Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()