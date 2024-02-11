import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class AdminPage(BasePage):

    PAGE_URL = Links.ADMIN_PAGE

    USERNAME_FIELD = ("xpath", '//*[@id="id_username"]')
    PASSWORD_FIELD = ("xpath", '//*[@id="id_password"]')
    SUBMIT_BUTTON = ("xpath", '//*[@id="login-form"]/div[3]/input')
    CAR_BUTTON = ("xpath", '/html/body/div/div[2]/div/div[1]/div[1]/div[1]/table/tbody/tr[2]/th/a')
    CHECKBOX_CLICK_ON = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/div[4]/table/tbody/tr[1]/td[6]/input')
    CHECKBOX_CLICK_OFF = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/div[4]/table/tbody/tr[2]/td[6]/input')
    CHECKBOX_CLICK_SETTINGS_ON_1 = ("xpath", '//*[@id="result_list"]/tbody/tr[2]/td[1]/input')
    CHECKBOX_CLICK_SETTINGS_ON_2 = ("xpath", '//*[@id="result_list"]/tbody/tr[3]/td[1]/input')
    CLICK_SETTINGS_SELECT = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/div[2]/label/select')
    CLICK_SETTINGS = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/div[2]/label/select/option[2]')
    CLICK_SETTINGS_BUTTON = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/div[2]/button')
    CLICK_SETTINGS_BUTTON_AGREEMENT = ("xpath", '/html/body/div/div[2]/div/div[1]/form/div/input[5]')
    SAVE = ("xpath", '/html/body/div/div[2]/div/div[1]/div/div/div[1]/form/p/input')

    # @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
        # time.sleep(2)
    # @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)
    # @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        time.sleep(1)

    def car_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CAR_BUTTON)).click()
        time.sleep(1)

    def checkbox_click_on(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CLICK_ON)).click()
        time.sleep(1)

    def checkbox_click_off(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CLICK_OFF)).click()
        time.sleep(1)

    def checkbox_click_settings_on_1(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CLICK_SETTINGS_ON_1)).click()
        time.sleep(1)

    def checkbox_click_settings_on_2(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CLICK_SETTINGS_ON_2)).click()
        time.sleep(1)

    def click_settings_select(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_SETTINGS_SELECT)).click()
        time.sleep(1)

    def click_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_SETTINGS)).click()
        time.sleep(1)

    def click_settings_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_SETTINGS_BUTTON)).click()
        time.sleep(1)

    def click_settings_button_agreement(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_SETTINGS_BUTTON_AGREEMENT)).click()
        time.sleep(1)

    def save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE)).click()
        time.sleep(1)