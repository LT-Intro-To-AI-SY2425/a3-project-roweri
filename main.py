from datetime import datetime, timedelta
# Q9PQI5FO67EYWG2P

import requests
from typing import List, Tuple, Callable, Any
from match import match
import os
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#ticker = "IBM"
#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey=Q9PQI5FO67EYWG2P"
#r = requests.get(url)

#json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
#with open("sample.json", "w") as outfile:
#    outfile.write(json_object)

with open('sample.json', 'r') as file:
    data = json.load(file)
def get_open(day):
    return data["Time Series (Daily)"][day[0]]["1. open"] if day[0] in data["Time Series (Daily)"] else None

def get_high(day):
    return data["Time Series (Daily)"][day[0]]["2. high"] if day[0] in data["Time Series (Daily)"] else None

def get_low(day):
    return data["Time Series (Daily)"][day[0]]["3. low"] if day[0] in data["Time Series (Daily)"] else None

def get_close(day):
    return data["Time Series (Daily)"][day[0]]["4. close"] if day[0] in data["Time Series (Daily)"] else None

def get_volume(day):
    #print(type(data["Time Series (Daily)"][day[0]]["5. volume"]), data["Time Series (Daily)"][day[0]]["5. volume"])
    return data["Time Series (Daily)"][day[0]]["5. volume"] if day[0] in data["Time Series (Daily)"] else None

def change_by_range(values):
    day1 = values[0]
    day2 = values[1]
    return abs((float(get_open([day1]))) - float(get_open([day2]))) if get_open([day2]) != None and get_open([day1]) != None else None

def buy_sell_hold(values):
    def get_date_x_days_ago(date_string, x):

        date_format = '%Y-%m-%d'
        given_date = datetime.strptime(date_string, date_format)

        five_days_ago = given_date - timedelta(days=x)

        result_date_string = five_days_ago.strftime(date_format)
        return result_date_string


    currentDate = data["Meta Data"]["3. Last Refreshed"]
    currentOpen = get_open([currentDate])
    
    previousDate = get_date_x_days_ago(currentDate, int(values[0]))

    max = 5
    c = 0

    while previousDate not in data["Time Series (Daily)"]:
        previousDate = get_date_x_days_ago(previousDate, 1).split(" ")[0]
        c += 1
        if c == 10: return None
    

    previousOpen = get_open([previousDate])

    if currentOpen == None or previousOpen == None: return None

    percentChange = (float(currentOpen) - float(previousOpen)) / float(previousOpen) * 100

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
    (str.split("what should i do looking _ days ago"), buy_sell_hold),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:

    for pattern, actual in pa_list:
        value = match(pattern, src)
        if value != None:
            pd = actual(value)
            if pd != None:
                return [pd]
            return ["I Dont Know"]
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