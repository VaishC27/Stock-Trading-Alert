import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_alpha_vantage_api_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH = "your_twilio_auth_token"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Get the stock price difference

# Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yes_closing = yesterday_data["4. close"]
print(yes_closing)

# Get the day before yesterday's closing stock price
day_before_yes_data = data_list[1]
day_before_yes_closing = day_before_yes_data["4. close"]
print(day_before_yes_closing)

# Find the positive difference
diff = float(yes_closing) - float(day_before_yes_closing)
up_down = "🔺" if diff > 0 else "🔻"

# Work out the percentage difference
diff_percent = round((diff / float(yes_closing)) * 100)
print(diff_percent)

# If percentage is greater than 5 then print("Get News")
if abs(diff_percent) > 1:
    print("Get News!")

    # STEP 2: Get news articles

    # Use the News API to get articles related to the COMPANY_NAME
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get the first 3 articles
    three_articles = articles[:3]
    print(three_articles)

    # STEP 3: Send news via Twilio

    # Create a new list of the first 3 article's headline and description using list comprehension
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    # Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="your-twilio-phone-number",
            to="your-personal-phone-number"
        )
else:
    print("No significant stock price change. No news fetched.")
