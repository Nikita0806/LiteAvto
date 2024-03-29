import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):             # сам тест

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.login                          # для пайтеста обозначения (маркер)
    def test_login(self):         # методы :
        self.dashboard_login_page.open()
        self.dashboard_login_page.is_opened()         # проверка открытия страницы
        self.dashboard_login_page.click_login()    # нажатие кнопки
        self.login_page.open()                  # открытие страницы
        self.login_page.enter_login(self.data.LOGIN)    # ввод логина
        self.login_page.enter_password(self.data.PASSWORD)  # ввод пароля
        self.login_page.click_submit_button()   # нажатие на кнопку
        # self.dashboard_page.select()
        # self.dashboard_page.select_marka()
        # self.dashboard_page.is_opened()         # проверка открытия страницы
        # self.dashboard_page.click_my_info_link()    # нажатие кнопки
        # self.personal_page.is_opened()          # открылась страница проверка
        # self.personal_page.change_name(f"Test {random.randint(1, 100)}")    # для ввода разных имен
        # self.personal_page.save_changes()       # сохраняем новое имя
        # self.personal_page.is_changes_saved()   # проверяем сохраненность
        # self.personal_page.make_screenshot("Success")   #