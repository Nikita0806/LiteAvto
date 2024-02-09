import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class SearchMarka(BasePage):                                      # локаторы для логина

    PAGE_URL = Links.DASHBOARD_PAGE

    SEARCH_MARKA = ("xpath", "/html/body/div[2]/form/p[2]/select")
    SELECT_MARKA = ("xpath", "/html/body/div[2]/form/p[2]/select/option[5]")     # Mazda
    SEARCH_MODEL = ("xpath", "/html/body/div[2]/form/p[3]/select")
    SELECT_MODEL = ("xpath", "/html/body/div[2]/form/p[3]/select/option[11]")    # 6
    SEARCH_CUZOV = ("xpath", "/html/body/div[2]/form/p[4]/select")
    SELECT_CUZOV = ("xpath", "/html/body/div[2]/form/p[4]/select/option[3]")     # Седан
    EXPLORE_BUTTON = ("xpath", "/html/body/div[2]/form/button")                  # Искать
    CAR_CARD = ("xpath", "/html/body/div[2]/ul/li/a")                            # Карточка авто
    START_PRICE = ("xpath", "/html/body/div[2]/form/p[8]/input")                 # Цена от
    END_PRICE = ("xpath", "/html/body/div[2]/form/p[7]/input")                   # Цена до
    START_MILEAGE = ("xpath", "/html/body/div[2]/form/p[9]/input")               # Пробег от
    END_MILEAGE = ("xpath", "/html/body/div[2]/form/p[10]/input")                # Пробег до


    # @allure.step("Click submit button")                         #для алюра
    def click_search_marka(self):                              # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MARKA)).click()
        # time.sleep(1)

    # @allure.step("Click submit button")                         #для алюра
    def click_select_marka(self):                              # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MARKA)).click()
        # time.sleep(1)

    # @allure.step("Click submit button")                         #для алюра
    def click_search_model(self):                              # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_MODEL)).click()
        # time.sleep(1)

    # @allure.step("Click submit button")                         #для алюра
    def click_select_model(self):                              # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SELECT_MODEL)).click()
        # time.sleep(1)

    # @allure.step("Click submit button")                         #для алюра
    def click_search_cuzov(self):  # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_CUZOV)).click()
        # time.sleep(1)

        # @allure.step("Click submit button")                         #для алюра
    def click_select_cuzov(self):  # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CUZOV)).click()
        # time.sleep(1)

    def start_price(self, new_price):  # для смены текста в поле
        self.wait.until(EC.element_to_be_clickable(self.START_PRICE)).send_keys(new_price)  #
        time.sleep(1)

    def end_price(self, new_price):  # для смены текста в поле
        self.wait.until(EC.element_to_be_clickable(self.END_PRICE)).send_keys(new_price)  #
        time.sleep(1)

    def start_mileage(self, new_mileage):  # для смены текста в поле
        self.wait.until(EC.element_to_be_clickable(self.START_MILEAGE)).send_keys(new_mileage)  #
        time.sleep(1)

    def end_mileage(self, new_mileage):  # для смены текста в поле
        self.wait.until(EC.element_to_be_clickable(self.END_MILEAGE)).send_keys(new_mileage)  #
        time.sleep(1)

        # @allure.step("Click submit button")                         #для алюра
    def explore_search(self):  # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.EXPLORE_BUTTON)).click()
        time.sleep(2)

    # @allure.step("Click submit button")                         #для алюра
    def car_card(self):  # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.CAR_CARD)).click()
        time.sleep(5)


