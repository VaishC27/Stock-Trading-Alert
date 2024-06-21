# Stock-Trading-Alert
This Python script checks the daily stock price changes of a specified company (e.g., Tesla Inc.) and sends news updates via SMS if the stock price changes significantly.

## Features

- Fetches daily stock prices using the Alpha Vantage API.
- Calculates the percentage change in stock prices.
- Retrieves the latest news articles related to the company if the stock price change exceeds a specified threshold.
- Sends news headlines and brief descriptions via SMS using the Twilio API.

## Prerequisites

- Python 3.x
- `requests` library
- `twilio` library
- Alpha Vantage API Key
- News API Key
- Twilio Account SID and Auth Token

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stock-news-notifier.git
    cd stock-news-notifier
    ```

2. Install the required Python packages:
    ```bash
    pip install requests twilio
    ```

3. Set up your environment variables or update the script with your API keys and phone numbers.

## Usage

1. Update the script with your API keys and phone numbers:
    ```python
    STOCK_NAME = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    STOCK_API_KEY = "your_alpha_vantage_api_key", reference: "https://www.alphavantage.co/support/#api-key"
    NEWS_API_KEY = "your_news_api_key", reference: "https://newsapi.org/account"
    TWILIO_SID = "your_twilio_sid", reference: "https://console.twilio.com"
    TWILIO_AUTH = "your_twilio_auth_token"
    ```

2. Run the script:
    ```bash
    python stock_news_notifier.py
    ```

## How It Works

1. **Fetch Stock Prices**: Retrieves the closing stock prices for the last two days.
2. **Calculate Change**: Computes the percentage difference between the two closing prices.
3. **Check Threshold**: If the price change exceeds 5%, it fetches the latest news articles about the company.
4. **Send SMS**: Sends the top 3 news articles' headlines and descriptions via Twilio SMS.

## Example Output

If the stock price change is significant, the script will send SMS messages formatted like this:

```
TSLA: 🔺2%
Headline: Tesla's new breakthrough in battery technology.
Brief: Tesla Inc. has announced a significant breakthrough in battery technology, promising longer ranges and faster charging times.
```


Feel free to customize this README file further based on your preferences and the specifics of your project.
