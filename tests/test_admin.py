import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):             # сам тест

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.admin                          # для пайтеста обозначения (маркер)
    def test_admin(self):
        # host
        self.search.open()
        self.search.scrol_down_button()
        self.search.next_page()
        # admin
        self.admin_page.open()
        self.admin_page.enter_login(self.data.LOGIN)
        self.admin_page.enter_password(self.data.PASSWORD)
        self.admin_page.click_submit_button()
        self.admin_page.car_button()
        self.admin_page.checkbox_click_settings_on()
        self.admin_page.click_settings_select()
        self.admin_page.click_settings()
        self.admin_page.click_settings_button()
        self.admin_page.click_settings_button_agreement()
        self.admin_page.checkbox_click_on()
        self.admin_page.checkbox_click_off()
        self.admin_page.scrol_down()
        self.admin_page.save_button()
        # host
        self.search.open()
        self.search.scrol_down_button()
        self.search.next_page()
