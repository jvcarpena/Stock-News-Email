# Stock and News Alert Script

This Python script monitors stock price changes and sends email alerts with relevant news if the price fluctuates by more than 5%.

## Features
- Fetches stock price data from an API
- Retrieves top 3 news articles if the stock price changes significantly
- Sends an email notification with the news summary

## Requirements
- Python 3
- `requests`, `python-dotenv`, `smtplib`

## Setup
1. Install dependencies:
   ```sh
   pip install requests python-dotenv
   ```
2. Create a `.env` file with the following:
   ```sh
   my_email=your_email@example.com
   my_password=your_password
   STOCK=TSLA
   COMPANY_NAME=Tesla
   NEWS_API_KEY=your_news_api_key
   STOCK_PRICE_API_KEY=your_stock_api_key
   STOCK_API=your_stock_api_url
   NEWS_API=your_news_api_url
   RECEIVER_EMAIL=receiver@example.com
   ```
3. Run the script:
   ```sh
   python script.py
   ```

