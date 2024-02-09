import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):             # сам тест

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.login                          # для пайтеста обозначения (маркер)
    def test_change_profile_name(self):         # методы :
        self.search.open()
        self.search.is_opened()         # проверка открытия страницы
        self.search.scrol_down_button()
        self.search.next_page()
        self.search.scrol_down()
        self.search.scrol_up()
        self.search.click_search_marka()    # нажатие кнопки
        self.search.click_select_marka()
        self.search.click_search_model()
        self.search.click_select_model()
        self.search.click_search_cuzov()
        self.search.click_select_cuzov()
        self.search.start_price(f"26{random.randint(1000, 100000)}")
        self.search.end_price(f"3{random.randint(10000, 1000000)}")
        self.search.start_mileage(f"46{random.randint(10, 1000)}")
        self.search.end_mileage(f"5{random.randint(100, 10000)}")
        self.search.explore_search()
        self.search.car_card()
        self.search.scrol_down()

