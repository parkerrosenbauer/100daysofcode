# Day 50 of 100 Days of Code Challenge
# Tinder Swiping Bot

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions


# facebook email
EMAIL = "parkerrosenbauer@gmail.com"

# setup for selenium
chrome_driver_path = "C:/Users/delph/OneDrive/Documents/1/chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# logging into tinder
driver.get("https://tinder.com")
# login button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/'
                                                            'div/div/header/div/div[2]/div[2]/a'))).click()
tinder_page = driver.window_handles[0]

# login with facebook
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span'
                                                            '/div[2]/button/span[2]'))).click()
fb_login_popup = driver.window_handles[1]

driver.switch_to.window(fb_login_popup)
driver.find_element(By.NAME, "email").send_keys(EMAIL)
driver.find_element(By.NAME, "pass").send_keys(os.environ.get("PASS"))
driver.find_element(By.NAME, "login").click()

# remove starting popup notifications
driver.switch_to.window(tinder_page)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="s18585620"]/div/div/div/div/div[3]/'
                                                            'button[1]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="s18585620"]/div/div/div/div/div[3]/'
                                                            'button[1]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="s1746966696"]/div/div[2]/div/div/div[1]/div[1]/'
                                                            'button'))).click()

# like a profile


def swipe_like_its_hot():
    can_swipe = True
    while can_swipe:
        try:
            # add a delay so tinder doesn't know I'm a sneaky bot
            driver.implicitly_wait(2)
            # attempt to click the like button
            driver.find_element(By.XPATH,'//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div'
                                         '/div[4]/div/div[4]/button').click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            # in case my little snake profile gets a match
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "BACK TO TINDER"))).click()

        except selenium.common.exceptions.NoSuchElementException:
            # in case I run out of swipes
            can_swipe = False


swipe_like_its_hot()




