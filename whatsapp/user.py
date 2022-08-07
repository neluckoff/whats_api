import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from whatsapp.client import Client


class User:

    def __init__(self, bot: Client) -> None:
        super().__init__()
        self.bot = bot
        self.driver = bot.driver
        self.account_info = self.__get_info()

    def logout(self) -> None:
        self.driver.get('https://web.whatsapp.com')

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='menu']"))).click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-testid='mi-logout menu-item']"))).click()

        WebDriverWait(self.bot.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='popup-controls-ok']"))).click()

        self.driver.close()
        self.driver.quit()

    def get_name(self) -> str:
        name = self.account_info[0]
        return name

    def get_status(self) -> str:
        status = self.account_info[1]
        return status

    def __get_info(self) -> list:
        self.driver.get('https://web.whatsapp.com')

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='default-user']"))).click()

        all_info = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='col-main-profile-input']")))

        info = []
        for elem in all_info:
            info.append(elem.text)
        return info

    def __get_edit_buttons(self) -> list:
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='default-user']"))).click()

        buttons = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span[data-testid='pencil']")))

        return buttons

    def set_name(self, name: str) -> None:
        self.driver.get('https://web.whatsapp.com')

        edit = self.__get_edit_buttons()[0]
        edit.click()

        info = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='col-main-profile-input']")))
        info[0].clear()
        info[0].send_keys(name)

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='checkmark']"))).click()

    def set_status(self, status: str) -> None:
        self.driver.get('https://web.whatsapp.com')

        edit = self.__get_edit_buttons()[1]
        edit.click()

        info = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='col-main-profile-input']")))
        info[1].clear()
        info[1].send_keys(status)

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-testid='checkmark']"))).click()
