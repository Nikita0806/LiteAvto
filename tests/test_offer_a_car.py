import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):             # сам тест

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.login                          # для пайтеста обозначения (маркер)
    def test_change_profile_name(self):
        self.dashboard_offer_page.open()                        #
        self.dashboard_offer_page.is_opened()                   #
        self.dashboard_offer_page.click_login()                 #
        self.login_page.open()                                  #  логин
        self.login_page.enter_login(self.data.LOGIN)            #
        self.login_page.enter_password(self.data.PASSWORD)      #
        self.login_page.click_submit_button()                   #
        # Страница оффера
        self.dashboard_offer_page.open()
        self.dashboard_offer_page.is_opened()
        self.dashboard_offer_page.click_offer()
        self.offer_page.scrol_save_button()
        self.offer_page.scrol_up()
        # Заполнение анкеты
        self.offer_page.click_search_marka()
        self.offer_page.click_select_marka()
        self.offer_page.click_search_model()
        self.offer_page.click_select_model()
        self.offer_page.click_search_cuzov()
        self.offer_page.click_select_cuzov()
        self.offer_page.enter_color('Серый')
        self.offer_page.enter_vin('VIN777C37')
        self.offer_page.enter_equipment('2')
        self.offer_page.click_search_date()
        self.offer_page.click_select_date()
        self.offer_page.scrol_down()
        self.offer_page.enter_price('1500000')
        self.offer_page.enter_mileage('130000')
        self.offer_page.click_search_transmission()
        self.offer_page.click_select_transmission()
        self.offer_page.click_search_engine_capacity()
        self.offer_page.click_select_engine_capacity()
        self.offer_page.click_search_engine_type()
        self.offer_page.click_select_engine_type()
        self.offer_page.click_search_drive_unit()
        self.offer_page.click_select_drive_unit()
        self.offer_page.click_search_state()
        self.offer_page.click_select_state()
        self.offer_page.scrol_down()
        self.offer_page.enter_horsepower('168')
        self.offer_page.click_search_pts()
        self.offer_page.click_select_pts()
        self.offer_page.enter_owners('4')
        self.offer_page.click_search_accounting()
        self.offer_page.click_select_accounting()
        self.offer_page.enter_telephone('79010334445')
        self.offer_page.scrol_down()
        self.offer_page.photo_1()
        self.offer_page.photo_2()
        self.offer_page.photo_3()
        self.offer_page.enter_description('Отличная тачка')
        self.offer_page.save_button()


