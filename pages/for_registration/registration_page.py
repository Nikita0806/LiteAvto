import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):                                      # локаторы для логина

    PAGE_URL = Links.REGISTRATION_PAGE                                 #

    USERNAME_FIELD = ("xpath", "/html/body/form/div/p[2]/input")     # локатор - место
    PASSWORD_FIELD = ("xpath", "/html/body/form/div/p[3]/input")     # локатор
    REPEAT_PASSWORD_FIELD = ("xpath", "/html/body/form/div/p[4]/input")     # локатор
    SUBMIT_BUTTON = ("xpath", "/html/body/form/div/button")       # локатор
    # @allure.step("Enter login")                                 # для алюра
    def enter_login(self, login):                               # принимает логин
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
        # time.sleep(2)
    # @allure.step("Enter password")                              #для алюра
    def enter_password(self, password):                         # принимает пароль
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)
    def enter_repeat_password(self, password):                         # принимает пароль
        self.wait.until(EC.element_to_be_clickable(self.REPEAT_PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)
    # @allure.step("Click submit button")                         #для алюра
    def click_submit_button(self):                              # нажимает на кнопку
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        time.sleep(2)