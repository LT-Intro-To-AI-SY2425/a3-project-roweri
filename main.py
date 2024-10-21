# API Key:
# Q9PQI5FO67EYWG2P

import requests
from typing import List, Tuple, Callable, Any
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker = "IBM"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey=Q9PQI5FO67EYWG2P"
r = requests.get(url)
data = r.json()

print(data)

def get_open(day: str):
    return data[day]["1. open"]

def get_high(day: str):
    return data[day]["2. high"]

def get_low(day: str):
    return data[day]["3. low"]

def get_close(day: str):
    return data[day]["4. close"]

def get_volume(day: str):
    return data[day]["5. volume"]

def change_by_range(day1: str, day2: str):
    return abs((get_open(day1)) - (get_open(day2)))

def buy_sell_hold():
    currentDate = data["Meta Data"]["3. Last Refreshed"]
    
def buy_action():
    print("see you later alligator")

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what was the volume on _"), get_volume),
    (str.split("what was the high on _"), get_high),
    (str.split("what was the low on _"), get_low),
    (str.split("what was the open on _"), get_open),
    (str.split("what was the close on _"), get_close),
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("what was the change between _ and _"), change_by_range),
    (str.split("what should I do"), buy_sell_hold),
    (["bye"], bye_action),
]