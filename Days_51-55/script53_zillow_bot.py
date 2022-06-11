from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import re

CHROME_DRIVER_PATH = "C:/Users/delph/OneDrive/Documents/1/chromedriver.exe"

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearch" \
      "Term%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%" \
      "22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filter" \
      "State%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%" \
      "22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc" \
      "%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse" \
      "%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A" \
      "872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.5005.63 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,sv;q=0.7",
}
DATA_LOCATION = "https://forms.gle/NNryaXAuHgSH9B846"


class ZillowScraper:
    def __init__(self):
        self.service = ChromeService(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        r = requests.get(url=URL, headers=HEADER)
        self.soup = BeautifulSoup(r.text, "html.parser")
        self.listings = self.soup.select("li article.list-card")
        self.addresses = []
        self.prices = []
        self.links = []

    def remove_bad_listing(self, info, indx):
        self.listings.pop(indx)
        try:
            self.addresses.pop(indx)
        except IndexError:
            pass
        try:
            self.links.pop(indx)
        except IndexError:
            pass
        try:
            self.prices.pop(indx)
        except IndexError:
            pass

    def get_links(self):
        listing_links = [link.find(name="a", class_="list-card-link") for link in self.listings]

        for data in listing_links:
            if data is None:
                self.remove_bad_listing(data, listing_links.index(data))
                listing_links.remove(data)
            elif "https" in data['href']:
                self.links.append(data['href'])
            else:
                new_link = "https://www.zillow.com" + data['href']
                self.links.append(new_link)

    def get_addresses(self):
        listing_addresses = [address.find(name="address", class_="list-card-addr") for address in self.listings]

        for data in listing_addresses:
            if data is None:
                self.remove_bad_listing(data, listing_addresses.index(data))
                listing_addresses.remove(data)
            else:
                self.addresses.append(data.text)

    def get_prices(self):
        listing_prices = [price.find(name="div", class_="list-card-price") for price in self.listings]

        for data in listing_prices:
            if data is None:
                self.remove_bad_listing(data, listing_prices.index(data))
                listing_prices.remove(data)
            else:
                price = re.findall(r'\$\d,\d{3}', data.text)[0]
                self.prices.append(price)

    def upload_data(self):
        self.driver.get(DATA_LOCATION)
        for item in range(len(self.listings)):
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/'
                                               'div/div[1]/input').send_keys(self.addresses[item])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/'
                                               'div/div[1]/input').send_keys(self.prices[item])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
                                               'div/div[1]/input').send_keys(self.links[item])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/'
                                               'span').click()
            self.driver.find_element(By.LINK_TEXT, "Submit another response").click()

