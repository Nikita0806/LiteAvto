import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardRegistrationPage(BasePage):                              # локаторы для главной страницы

    PAGE_URL = Links.DASHBOARD_PAGE                         #

    REGISTRATION_BATTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[1]")  # нужная кнопка

    # @allure.step("Click on 'My Info' link")                 # для алюра
    def click_registration(self):                           # нажимаем на нужную кнопку
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_BATTON)).click()
        # time.sleep(2)

