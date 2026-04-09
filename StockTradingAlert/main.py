import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from twilio.rest import Client

env_path = Path("/Users/jasnaassim/PycharmProjects/100 Days/Stock/.venv/.env")
load_dotenv(dotenv_path=env_path)

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

if not ACCOUNT_SID or not AUTH_TOKEN:
    raise ValueError("Missing credentials in .env file")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    'q': COMPANY_NAME,
    'from': '2026-03-08',
    'sortBy': 'publishedAt',
    'apiKey': 'API'
}

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'outputsize': 'compact',
    'apikey': 'API'
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()
data_to_list = [value for (key, value) in data.items()]
print(data)
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Extract time series data
time_series = data.get('Time Series (Daily)', {})
dates = sorted(time_series.keys(), reverse=True)  # Most recent first

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()
first_3_news = news_data['articles'][:3]

if len(dates) >= 2:
    # Get yesterday and day before yesterday closing prices
    yesterday_close = float(time_series[dates[0]]['4. close'])
    day_before_close = float(time_series[dates[1]]['4. close'])

    # Calculate percentage change
    percentage_change = ((yesterday_close - day_before_close) / day_before_close) * 100

    print(f"Yesterday ({dates[0]}): ${yesterday_close}")
    print(f"Day Before ({dates[1]}): ${day_before_close}")
    print(f"Percentage Change: {percentage_change:.2f}%")

    # Check if change is >= 5% (increase or decrease)
    if abs(percentage_change) <= 5:
        #print(first_3_news)
        first_three_tuples = [
            (article['title'], article['description'])
            for article in first_3_news
        ]
        #print(first_three_tuples)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

        messages = [
            client.messages.create(
                body=f"{article['title']}\n\n{article['description']}",
                from_="+xxxxxxxxxx",
                to="+1xxxxxxxxxx"
            )
            for article in first_3_news
        ]
#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

