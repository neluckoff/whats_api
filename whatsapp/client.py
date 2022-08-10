import getpass
import pickle
import re
import os
import time

from qrcode import make
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import quote


class Client:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.__set_options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        pickle.dump(self.driver.get_cookies(), open("../cookies", "wb"))
        self.cookies = pickle.load(open("../cookies", "rb"))

        self.__login()

    def __set_options(self):
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 "
                                  "Firefox/84.0")
        self.options.add_argument("--user-data-dir=C:\\Users\\neluc\\AppData\\Local\\Google\\Chrome\\User "
                                  "Data\\Default".format(getpass.getuser()))
        self.options.headless = True  # makes the browser invisible

    def __login(self):
        self.driver.get('https://web.whatsapp.com')

        for i in self.cookies:
            self.driver.add_cookie(i)

        try:
            value = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='qrcode']")))
            value = value.get_attribute('data-ref')

            print('Scan the QR code through the official WhatsApp application to authorize your account.')
            make(value).save("qr.png")
            img = Image.open('qr.png')
            img.show()

            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='default-user']")))
                pickle.dump(self.driver.get_cookies(), open("../cookies", "wb"))
                img.close()
                os.remove('qr.png')
                print('Authorization was successful')
            except TimeoutException:
                print('Authorization timed out')
                img.close()
                os.remove('qr.png')
                self.driver.close()
                self.driver.quit()

        except TimeoutException:
            print('User is authorized, authorization is not required')

    def __check_phone_number(self, phone: str) -> str:
        result = [abs(int(s)) for s in re.findall(r'-?\d+\.?\d*', phone)]
        text = ''
        for i in result:
            text += str(i)
        return text

    def __get_driver(self):
        return self.driver

    def message_send(self, phone_number: str, message: str) -> None:
        phone = self.__check_phone_number(phone_number)

        self.driver.get(f'https://web.whatsapp.com/send?phone={phone}&text={quote(message)}')
        submit = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='compose-btn-send']")))
        submit.click()
        time.sleep(1)
