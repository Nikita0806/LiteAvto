import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardLoginPage(BasePage):                              # локаторы для главной страницы

    PAGE_URL = Links.DASHBOARD_PAGE                         #

    LOGIN_BATTON = ("xpath", "/html/body/div[1]/ul/li[5]/a[2]")  # нужная кнопка
    # SELECT = ("xpath", "/html/body/div[2]/form/p[2]/select")
    # v = ("xpath", "/html/body/div[2]/form/p[2]/select/option[2]")

    # @allure.step("Click on 'My Info' link")                 # для алюра
    def click_login(self):                           # нажимаем на нужную кнопку
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BATTON)).click()
        # time.sleep(2)

    # def select(self):  # нажимаем на нужную кнопку                        перенести
    #     self.wait.until(EC.element_to_be_clickable(self.SELECT)).click()
    #     time.sleep(1)
    #
    # def select_marka(self):  # нажимаем на нужную кнопку
    #     self.wait.until(EC.element_to_be_clickable(self.v)).click()
    #     time.sleep(3)
