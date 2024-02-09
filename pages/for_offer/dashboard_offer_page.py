import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardOfferPage(BasePage):                              # локаторы для главной страницы

    PAGE_URL = Links.DASHBOARD_PAGE                         #

    LOGIN_BATTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[2]")         # логин
    OFFER_A_CAR_BUTTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[1]")   # предложить автомобиль

    # @allure.step("Click on 'My Info' link")                 # для алюра
    def click_login(self):                           # нажимаем на нужную кнопку
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BATTON)).click()
        # time.sleep(2)
    #
    # @allure.step("Click on 'My Info' link")                 # для алюра
    def click_offer(self):                           # нажимаем на нужную кнопку
        self.wait.until(EC.element_to_be_clickable(self.OFFER_A_CAR_BUTTON)).click()
        time.sleep(1)
