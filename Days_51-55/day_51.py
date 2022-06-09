# Day 51 of 100 Days of Code Challenge
# Twitter bot to tweet out my internet speeds

import os
from script51_twitter_bot import InternetSpeedTwitterBot

# constants
CHROME_DRIVER_PATH = "C:/Users/delph/OneDrive/Documents/1/chromedriver.exe"
TWITTER_PHONE = os.environ.get("TWITTER_PHONE")
TWITTER_PASS = os.environ.get("TWITTER_PASS")

twitter_bot = InternetSpeedTwitterBot(driver_path=CHROME_DRIVER_PATH)

twitter_bot.get_internet_speed()
print(twitter_bot.up)
print(twitter_bot.down)
twitter_bot.tweet_your_heart_out(login=TWITTER_PHONE, password=TWITTER_PASS)
