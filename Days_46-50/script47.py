# Day 47 of 100 Days of Code
# Amazon item price tracker
import os
import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B09ZY9NVHL/?coliid=I1P5S20GDRCSTP&colid=YEIF2ZIGUK8J&ref_=lv_ov_lig_dp_it&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.5005.63 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,sv;q=0.7",
}
PRICE_TO_BUY = 300.00
USER = "pythonbot97@gmail.com"

r = requests.get(url=URL, headers=HEADER)
amazon_data = r.text

soup = BeautifulSoup(amazon_data, "html.parser")
chair_price = float(soup.find(name="span", class_="a-price-whole").text +
                    soup.find(name="span", class_="a-price-fraction").text)

if chair_price < PRICE_TO_BUY:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=os.environ.get("PASS"))
        connection.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg=f"Subject:Your Amazon Chair is on sale\n\nThe current price is {chair_price}, which is less than your "
                f"predetermined buy price of {PRICE_TO_BUY}")

