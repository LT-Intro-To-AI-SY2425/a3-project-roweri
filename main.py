# API Key:
# Q9PQI5FO67EYWG2P

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker = "IBM"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=Q9PQI5FO67EYWG2P"
r = requests.get(url)
data = r.json()

print(data)