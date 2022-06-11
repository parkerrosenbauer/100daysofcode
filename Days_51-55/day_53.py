# Day 53 of 100 Days of Code Challenge
# Capstone Project: Zillow rental price spreadsheet (data entry automation)

from script53_zillow_bot import ZillowScraper

data = ZillowScraper()
data.get_links()
data.get_addresses()
data.get_prices()
data.upload_data()
