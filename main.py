# API Key:
# Q9PQI5FO67EYWG2P

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker = "IBM"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey=Q9PQI5FO67EYWG2P"
r = requests.get(url)
data = r.json()

print(data)

def get_high(day: dict):
    return day

def volume_on_day():
    pass


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what was the volume on _"), volume_on_day),
    (str.split("what was the high on _"), high_on_day),
    (str.split("what was the low on _"), low_on_day),
    (str.split("what was the open on _"), open_on_day),
    (str.split("what was the close on _"), close_on_day),
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("what was the change between _ and _"), change_by_range),
    (str.split("what should I do"), buy_sell_hold),
    (["bye"], bye_action),
]