import matplotlib.pyplot as plt

def plot_price_trend(df, token_name):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['price'], label=f'{token_name} Price', color='blue')
    plt.title(f'{token_name} Price Trend (Last 90 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()