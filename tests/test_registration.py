import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):             # сам тест

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.registration                          # для пайтеста обозначения (маркер)
    def test_change_profile_name(self):         # методы :
        self.dashboard_registration_page.open()
        self.dashboard_registration_page.is_opened()         # проверка открытия страницы
        self.dashboard_registration_page.click_registration()    # нажатие кнопки
        self.registration_page.open()                  # открытие страницы
        self.registration_page.enter_login(self.data.R_LOGIN)    # ввод логина
        self.registration_page.enter_password(self.data.R_PASSWORD)  # ввод пароля
        self.registration_page.enter_repeat_password(self.data.R_REPEAT_PASSWORD)  # ввод пароля
        self.registration_page.click_submit_button()   # нажатие на кнопку
