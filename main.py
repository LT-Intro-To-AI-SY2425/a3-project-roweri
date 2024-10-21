from datetime import datetime, timedelta
# Q9PQI5FO67EYWG2P

import requests
from typing import List, Tuple, Callable, Any
from match import match
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker = "IBM"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey=Q9PQI5FO67EYWG2P"
r = requests.get(url)
data = r.json()

def get_open(day: str):
    return data[day]["1. open"]

def get_high(day: str):
    return data[day]["2. high"]

def get_low(day: str):
    return data[day]["3. low"]

def get_close(day: str):
    return data[day]["4. close"]

def get_volume(day: str):
    print(data[day[0]])
    return data[day[0]]["5. volume"] if day[0] in data else None

def change_by_range(day1: str, day2: str):
    return abs((get_open(day1)) - (get_open(day2)))

def buy_sell_hold():
    def get_date_x_days_ago(date_string, x):

        date_format = '%Y-%m-%d'
        given_date = datetime.strptime(date_string, date_format)

        five_days_ago = given_date - timedelta(days=x)

        result_date_string = five_days_ago.strftime(date_format)
        return result_date_string


    currentDate = data["Meta Data"]["3. Last Refreshed"]
    currentOpen = get_open(currentDate)
    
    previousDate = get_date_x_days_ago(currentDate, 5)

    while previousDate not in data:
        previousDate = get_date_x_days_ago(previousDate, 1)
    

    previousOpen = get_open(previousDate)

    percentChange = (currentOpen - previousOpen) / previousOpen * 100

    if percentChange >= 3.0:
        return "Sell!"
    elif percentChange <= -3.0:
        return "Buy!"
    else:
        return "Hold!"
    
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

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

def search_pa_list(src: List[str]) -> List[str]:

    for pattern, actual in pa_list:
        value = match(pattern, src)
        if value != None:
            result = actual(value)
            if result:
                return result
            else:
                return ["No answers"]
    return ["I don't understand"]



def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()