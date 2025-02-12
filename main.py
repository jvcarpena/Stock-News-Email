import os
from dotenv import load_dotenv
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load env file
load_dotenv()

my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
STOCK = os.getenv("STOCK")
COMPANY_NAME = os.getenv("COMPANY_NAME")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_PRICE_API_KEY = os.getenv("STOCK_PRICE_API_KEY")

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY
}
stock_response = requests.get(url=os.getenv("STOCK_API"), params=stock_price_parameters)
stock_response.raise_for_status()
stock_price_data = stock_response.json()
print(stock_price_data)
yesterday_close_price = 1000  # for testing only.
day_before_yesterday_price = 800  # for testing only.

percentage = round((yesterday_close_price - day_before_yesterday_price) / yesterday_close_price * 100, 2)

up_down = None
if percentage > 0:
    up_down = "+"
else:
    up_down = "-"


if abs(percentage) > 5:
    print("get news")

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=os.getenv("NEWS_API"), params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]  # Used to print the first three articles using python slicing
    three_articles = articles[:3]
    # print(three_articles)

    formatted_message = [f"Headline: {article['title']}.\nBrief: {article['description']}"
                         for article in three_articles]

    for article in formatted_message:  # Contains three messages.
        msg = MIMEMultipart()  # for creating an email message that can have multiple parts.
        msg['From'] = my_email
        msg['To'] = os.getenv("RECEIVER_EMAIL")
        msg['Subject'] = f"TSLA: {up_down}{percentage}%"

        body = article

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.send_message(msg)
