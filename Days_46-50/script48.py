# Day 48 of 100 Days of Code Challenge
# Selenium Webdriver Game Player
# Play the game at: https://orteil.dashnet.org/cookieclicker/

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# setup for selenium
chrome_driver_path = "C:/Users/delph/OneDrive/Documents/1/chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# opens the cookie clicker game and selects the language
driver.get("https://orteil.dashnet.org/cookieclicker/")
language = driver.find_element(By.ID, "langSelect-EN")
language.click()


def buy_product():
    """Buys the cookie products"""
    try:
        top_tier_products = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    except selenium.common.exceptions.NoSuchElementException:
        pass
    else:
        if len(top_tier_products) > 0:
            top_tier_products[-1].click()
            buy_product()


def buy_upgrade():
    """Buys the cookie upgrades"""
    try:
        upgrades = driver.find_element(By.CSS_SELECTOR, "#upgrades .enabled")
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    else:
        upgrades.click()


def cookie_clicker():
    """Clicks the cookies for 5 seconds at a time"""
    start_time = time.time()
    seconds = 5
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookieAnchor #bigCookie")
    while True:
        cookie.click()
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > seconds:
            break


def click_the_cookies():
    """Runs the cookie clicker game for 5 minutes, then prints the cookies made per second to evaluate the algorithm's
    performance"""
    start_time = time.time()
    seconds = 300
    while True:
        if time.time() - start_time > seconds:
            break
        else:
            cookie_clicker()
            buy_upgrade()
            buy_product()

    driver.quit()
    print("Final cookies made per second: " +
          driver.find_element(By.ID, "cookiesPerSecond").text.strip("per second: "))


click_the_cookies()
