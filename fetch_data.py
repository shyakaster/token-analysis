import pandas as pd
import numpy as np
import requests
from datetime import datetime

def fetch_crypto_data(token_id, days=90, currency='usd'):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
    params = {'vs_currency': currency, 'days': days, 'interval': 'daily'}
    response = requests.get(url, params=params)
    data = response.json()
    
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['returns'] = df['price'].pct_change()
    df['log_returns'] = np.log(df['price'] / df['price'].shift(1))
    return df