from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import dotenv
import time
import random

dotenv.load_dotenv()

INTERNET_SPEED_TEST_ENDPOINT = "http://speed.kt.com"
PROMISED_DOWN = 250

kt_id = "dudemanguy"
kt_password = os.environ.get("PASSWORD")

TWITTER_ENDPOINT = "https://twitter.com/"
TWITTER_HANDLE = "Jhe32795595"
TWITTER_EMAIL = "bgkt211@gmail.com"
TWITTER_PWD = os.environ.get("TWT_PASSWORD")

class InternetSpeedTwitterBot:

    def __init__(self):
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.down = PROMISED_DOWN
        self.speed = 0


    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_TEST_ENDPOINT)

        home_test_btn = self.driver.find_element(By.ID, "ifAreagiga_btn")
        home_test_btn.click()

        time.sleep(random.randint(2,3))

        base_window = self.driver.window_handles[0]
        kt_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(kt_login_window)

        id_input_field = self.driver.find_element(By.ID, "userId")
        id_input_field.send_keys(kt_id)

        pwd_input_field = self.driver.find_element(By.ID, "password")
        pwd_input_field.send_keys(kt_password)

        time.sleep(random.randint(2,3))

        login_submit = self.driver.find_element(By.ID, "loginSubmit")
        login_submit.click()

        time.sleep(random.randint(2,3))

        self.driver.switch_to.window(base_window)

        select_addrs = self.driver.find_element(By.XPATH, '//*[@id="ifArea"]/div/div/table[1]/tbody/tr/td/form/div/div[2]/div/label/span[1]/span')
        select_addrs.click()

        time.sleep(random.randint(2,3))

        start_btn = self.driver.find_element(By.ID, "measureBtn")
        start_btn.click()

        time.sleep(30)

        self.speed = self.driver.find_element(By.CLASS_NAME, "download-value").text

    def tweet_at_provider(self):

        ### login

        self.driver.get(TWITTER_ENDPOINT)

        time.sleep(random.randint(3, 4))

        twt_login_btn = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span')
        twt_login_btn.click()

        time.sleep(random.randint(3,4))

       

        twt_email_input = self.driver.find_element(By.NAME, "text")
        twt_email_input.send_keys(TWITTER_EMAIL)

        time.sleep(1)

        twt_email_input.send_keys(Keys.RETURN)

        time.sleep(1)

        twt_email_input = self.driver.find_element(By.NAME, "text")
        twt_email_input.send_keys(TWITTER_HANDLE)

        time.sleep(1)

        twt_email_input.send_keys(Keys.RETURN)

        time.sleep(1)

        twt_pwd_input = self.driver.find_element(By.NAME, "password")
        twt_pwd_input.send_keys(TWITTER_PWD)
        twt_pwd_input.send_keys(Keys.RETURN)

        time.sleep(random.randint(3,5))

        ### make tweet

        text_field = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')

        if int(self.speed) < self.down:
            text_field.send_keys(f"Hi KT, why is my internet speed {self.speed} when I pay for {self.down}?")

            time.sleep(random.randint(3, 5))

            tweet_btn = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/'
                                                 'div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet_btn.click()





        input("Enter..")