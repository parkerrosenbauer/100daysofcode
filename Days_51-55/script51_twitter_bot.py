from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = ChromeService(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button"))).click()
        sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_your_heart_out(self, login, password):
        message = f"Hey Twitter, my current internet speed is {self.down}down/{self.up}up. So fast!"
        self.driver.get("https://twitter.com/login")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]'
                      '/label/div/div[2]/div/input'))).send_keys(login, Keys.ENTER)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/'
                      'div[2]/div/label/div/div[2]/div[1]/input'))).send_keys(password, Keys.ENTER)

        sleep(5)
        create_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                          'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                          'div/div/div/div/div/div/div/div/label/div[1]/div/div/div/'
                                                          'div/div[2]/div/div/div/div')
        create_tweet.send_keys(message)

        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/'
                                           'div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
