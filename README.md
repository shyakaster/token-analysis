# Token Analysis Project

## Overview
This project is designed to analyze cryptocurrency tokens by fetching data, performing exploratory data analysis, computing financial indicators, and visualizing key trends. It is structured for **financial data analysts** looking to apply their skills in the **cryptocurrency domain**.

## Features
- Fetching real-time cryptocurrency data using CoinGecko API
- Exploratory Data Analysis (EDA) on price trends and returns
- Calculation of Moving Averages (SMA 20 & SMA 50)
- Volatility analysis using rolling standard deviation
- Risk assessment using **Sharpe Ratio**
- Data visualization using Matplotlib

## Project Structure
```
📂 Token Analysis Project
│── fetch_data.py           # Fetch cryptocurrency data from CoinGecko API
│── plot_price_trend.py     # Visualize price trends
│── moving_averages.py      # Compute and plot moving averages
│── volatility_analysis.py  # Compute and plot volatility
│── risk_analysis.py        # Compute financial risk indicators like Sharpe Ratio
│── main.py                 # Main script to run the analysis
│── README.md               # Documentation
│── requirements.txt        # Python dependencies
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/token-analysis.git
   cd token-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the main script to perform the full token analysis:
```sh
python main.py
```
This will:
- Fetch Bitcoin price data for the last 90 days
- Generate price trend charts
- Compute and visualize moving averages
- Analyze volatility
- Calculate the **Sharpe Ratio**

## Example Output
- **Bitcoin Price Trend**
- **Moving Averages** (20-day & 50-day)
- **Rolling Volatility**
- **Sharpe Ratio Calculation**

## Contributions
Feel free to fork and contribute to improve the analysis or support additional cryptocurrencies.

## License
This project is licensed under the MIT License.

## Contact
For inquiries, reach out via [LinkedIn](https://www.linkedin.com/in/ankusi/).

