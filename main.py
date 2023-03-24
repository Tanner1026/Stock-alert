import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_key = "7OB4B1NI4HX92GHS"
api_key_twilio = "55f9938e4423f53da9443d1a596c9c14"
account_sid = 'ACbad74a5a9d0fbcb68185e8568755f51f'
auth_token = 'b495f8cbe990a5ae0deccce58e65b91e'

url_stock = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={stock_key}'
r = requests.get(url_stock)
data_stock = r.json()

url_news = f'https://newsapi.org/v2/everything'
params_news = {"apiKey": '574562ea13364c03977d3b71db73dc9d',
               'language': 'en',
               'sortBy': 'relevancy',
                "q": {COMPANY_NAME}}
news = requests.get(url_news, params=params_news)

data = data_stock["Time Series (Daily)"]
yesterdays_date = [value for (key, value) in data.items()]
yesterday = float(yesterdays_date[0]['4. close'])
two_days = float(yesterdays_date[1]['4. close'])
percent_change = round(((yesterday - two_days) / two_days) * 100)


data_news = news.json()
articles = data_news['articles']
three_articles = articles[:3]


formatted_articles = [f"Headline: {articles['title']}. \nContext: {articles['description']}" for articles in three_articles]
client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+18885216329',
        to='+13852095577'
            )


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

