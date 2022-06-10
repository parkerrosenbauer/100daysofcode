from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from time import sleep

CHROME_DRIVER_PATH = "C:/Users/delph/OneDrive/Documents/1/chromedriver.exe"
URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.service = ChromeService(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.follow_buttons = []

    def login(self, user, password):
        self.driver.get(URL)
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(user)
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password,
                                                                                                          Keys.ENTER)

    def find_followers(self, account):
        sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div'
                                                  '/div[2]/input'))).send_keys(account)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div'
                                                  '/div[2]/div[3]/div/div[2]/div/div[1]/a'
                                        ))).click()

        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/snake.wild/followers/"]').click()

        sleep(5)
        # load accounts
        # scroll down the account popup 5 times only, otherwise we'd be here for a long time
        for _ in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # put all the follow buttons loaded into a list
        self.follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li > div div > button")

    def follow(self):
        for button in self.follow_buttons:
            # sleep inbetween clicks to not get bot clocked
            sleep(1)
            try:
                button.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                # if I've already followed the user a popup comes up asking if I'd like to unfollow,
                # so the bot will click cancel
                self.driver.find_element(By.CSS_SELECTOR, "div._a9-v > div._a9-z > button._a9_1").click()



