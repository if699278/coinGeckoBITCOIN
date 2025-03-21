import requests, pandas as pd, time 

def cur_price(ticker,api_key,currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ticker}&vs_currencies={currency}"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": api_key
    }
    response = requests.get(url, headers=headers)
    data=response.json()
    price=data[ticker][currency]
    return(price)

def all_crypto(api_key):
    url = f"https://api.coingecko.com/api/v3//coins/list"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": api_key
    }

    response = requests.get(url, headers=headers)

    lists=response.json()
    df = pd.DataFrame(lists, columns=['id','symbol','name'])
    return(df)
    #return(lists)

def historical_data(id_cryp,api_key,date,currency):
    url = f"https://api.coingecko.com/api/v3//coins/{id_cryp}/history?date={date}&localization=true"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": api_key
    }

    response = requests.get(url, headers=headers)

    lists=response.json()
    curr_price=lists['market_data']['current_price'][currency]
    return(curr_price)



def api_status(api_key):
    url = "https://api.coingecko.com/api/v3/ping"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": api_key
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    return(response.text)


def date_delta(start_dt,end_dt):
    from datetime import date, timedelta
    delta = timedelta(days=1)
    # store the dates between two dates in a list
    dates = []
    start=start_dt
    while start_dt <= end_dt:
        # add current date to list by converting  it to iso format
        #dates.append(start_dt.isoformat())
        dates.append(start_dt.strftime("%d-%m-%Y"))
        # increment start date by timedelta
        start_dt += delta
    print('Dates between', start, 'and', end_dt)
    return(dates)