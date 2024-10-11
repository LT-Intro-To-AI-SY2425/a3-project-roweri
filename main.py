# API Key:
# JJKIKNB87YX2HJA5

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=JJKIKNB87YX2HJA5'
r = requests.get(url)
data = r.json()

print(data)
