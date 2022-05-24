# Day 36 of 100 Days of Code Challenge
# Stock Trading News Alerts
# The goal of this program is to look at the closing price of stock from yesterday to the day before and send
# a text alert if the percent difference is higher or lower than 5% along with top news on the company

import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, FR
from twilio.rest import Client

STOCK = "WMT"
COMPANY_NAME = "Walmart"

# the values below have been replaced with dummy variables
alpha_vantage_key = "1234567" 
news_key = "1234567" 
account_sid = "1234567"
auth_token = "1234567" 


def top_article() -> tuple:
    """pull the top news article relating to the company of interest"""
    r = requests.get(url=f"https://newsapi.org/v2/top-headlines?"
                         f"q={COMPANY_NAME}"
                         f"&apiKey={news_key}")
    new_articles = r.json()
    top_three = new_articles["articles"][:1]
    title = top_three[0]["title"]
    desc = top_three[0]["description"]

    return title, desc


def format_alert(change: int, headline: str, brief: str) -> str:
    """formats the text alert"""
    if change > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    alert = f"{STOCK}: {symbol}{abs(change)}%\n" \
            f"Headline: {headline}\n" \
            f"Brief: {brief}"
    return alert


# pull stock data from alpha vantage api
response = requests.get(url=f"https://www.alphavantage.co/query?"
                            f"function=TIME_SERIES_DAILY"
                            f"&symbol={STOCK}"
                            f"&apikey={alpha_vantage_key}")
response.raise_for_status()
stock_data = response.json()

# get the values from the stock data json and calculate percent change
day_data = list(stock_data['Time Series (Daily)'].values())
yest_close_pr = float(day_data[0]["4. close"])
day_before_close_pr = float(day_data[1]["4. close"])
perc_change = round((yest_close_pr - day_before_close_pr) / day_before_close_pr * 100)

# determine if the percent change is noteworthy and if it is, send a text message
if perc_change <= -5 or perc_change >= 5:
    current = top_article()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=format_alert(perc_change, current[0], current[1]),
        from_="+17196314924",
        to="+15551205"  # not my real number
    )
