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

    def __init__(self, user_dir: str = None, expectation: int = 10) -> None:
        """
        WhatsApp account class

        :param:
            user_dir (str): the path to your Google profile on your computer
            (necessary in order to permanently not log in)

            Path Example for Windows:
            C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default

            expectation (int): the waiting time for the WhatsApp page to load,
            if the computer is weak - put more
        """
        self.options = webdriver.ChromeOptions()

        if user_dir is not None:
            path = f"--user-data-dir={user_dir}"
            self.options.add_argument(path.format(getpass.getuser()))

        self.__set_options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        pickle.dump(self.driver.get_cookies(), open("cookies", "wb"))
        self.cookies = pickle.load(open("cookies", "rb"))

        self.__login(expectation)

    def __set_options(self) -> None:
        """
        Applying browser settings
        """
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 "
                                  "Firefox/84.0")
        self.options.headless = True  # makes the browser invisible

    def __login(self, expectation: int) -> None:
        """
        Method for authorization in WhatsApp

        :param:
            expectation (int): the waiting time for the WhatsApp page to load
        """
        self.driver.get('https://web.whatsapp.com')

        for i in self.cookies:
            self.driver.add_cookie(i)

        try:
            value = WebDriverWait(self.driver, expectation).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='qrcode']")))
            value = value.get_attribute('data-ref')

            print('Scan the QR code through the official WhatsApp application to authorize your account.')
            make(value).save("qr.png")
            img = Image.open('qr.png')
            img.show()

            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='default-user']")))
                pickle.dump(self.driver.get_cookies(), open("cookies", "wb"))
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
        """
        Method to validate entered phone number

        :param:
            phone (str): phone number

        :return:
            str: changed phone number
        """
        result = [abs(int(s)) for s in re.findall(r'-?\d+\.?\d*', phone)]
        text = ''
        for i in result:
            text += str(i)
        return text

    def message_send(self, phone_number: str, message: str) -> None:
        """
        Method for sending a regular message to a phone number

        :param:
            phone_number (str): phone number
            message (str): text message
        """
        phone = self.__check_phone_number(phone_number)

        self.driver.get(f'https://web.whatsapp.com/send?phone={phone}&text={quote(message)}')
        submit = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='compose-btn-send']")))
        submit.click()
        time.sleep(1)
