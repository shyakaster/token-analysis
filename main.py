from fetch_data import fetch_crypto_data
from plot_price_trend import plot_price_trend
from moving_averages import compute_moving_averages, plot_moving_averages
from volatility_analysis import compute_volatility, plot_volatility
from risk_analysis import compute_sharpe_ratio

# Fetch data
btc_data = fetch_crypto_data('bitcoin', days=90)

# Plot price trend
plot_price_trend(btc_data, 'Bitcoin')

# Compute and plot moving averages
btc_data = compute_moving_averages(btc_data)
plot_moving_averages(btc_data, 'Bitcoin')

# Compute and plot volatility
btc_volatility = compute_volatility(btc_data)
plot_volatility(btc_volatility, 'Bitcoin')

# Compute Sharpe Ratio
sharpe_ratio = compute_sharpe_ratio(btc_data)
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Save the data
btc_data.to_csv('bitcoin_analysis.csv')
