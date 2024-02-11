import random
import allure
import pytest
from base.base_test import BaseTest

# @allure.feature("Profile Functionality")        # для алюра
class TestProfileFeature(BaseTest):

    # @allure.title("Change profile name")        # для алюра
    # @allure.severity("Critical")                # для алюра

    @pytest.mark.registration                          # для пайтеста обозначения (маркер)
    def test_full(self):
            # РЕГИСТРАЦИЯ
        self.dashboard_registration_page.open()                                     # Открытие главной страницы
        self.dashboard_registration_page.is_opened()                                # Проверка на открытие
        self.dashboard_registration_page.click_registration()                       # Клик на регистрация
        self.registration_page.open()                                               # Открытие страницы регистрации
        self.registration_page.enter_login(self.data.R_LOGIN)                       # ввод логина
        self.registration_page.enter_password(self.data.R_PASSWORD)                 # ввод пароля
        self.registration_page.enter_repeat_password(self.data.R_REPEAT_PASSWORD)   # ввод пароля
        self.registration_page.click_submit_button()                                # Клик на кнопку сохранить
        self.registration_page.exit_login()                                         # Выход из логина
            # ЛОГИН
        self.login_page.enter_login(self.data.R_LOGIN)                              # ввод логина
        self.login_page.enter_password(self.data.R_PASSWORD)                        # ввод пароля
        self.login_page.click_submit_button()                                       # нажатие на войти
            # ФИЛТЕР
        self.search.scrol_down_button()                                             # Скролл страницы до кнопки
        self.search.next_page()                                                     # Следующая страница
        self.search.scrol_down()                                                    # Скролл вниз
        self.search.scrol_up()                                                      # Скролл вверх
        self.search.click_search_marka()                                            # Выпадающий список марок
        self.search.click_select_marka()                                            # Выбор марки
        self.search.click_search_model()                                            # Выпадающий список модели
        self.search.click_select_model()                                            # Выбор модели
        self.search.click_search_cuzov()                                            # Выпадающий список кузовов
        self.search.click_select_cuzov()                                            # Выбор кузова
        self.search.start_price(f"26{random.randint(1000, 100000)}")                # Заполнение цены от
        self.search.end_price(f"3{random.randint(10000, 1000000)}")                 # Заполнение цены до
        self.search.start_mileage(f"46{random.randint(10, 1000)}")                  # Заполнение пробега от
        self.search.end_mileage(f"5{random.randint(100, 10000)}")                   # Заполнение пробега до
        self.search.explore_search()                                                # Поиск
        self.search.car_card_1()                                                    # Открытие карточки авто
        self.search.scrol_down()                                                    # Скролл в карточке авто вниз
        self.search.scrol_up()                                                      # Скролл в карточке авто вверх
            # ДОБВАЛЕНИЕ АВТОМОБИЛЯ
        self.dashboard_offer_page.click_offer()                                     # Клик добавление автомобил
        self.offer_page.scrol_save_button()                                         # Скролл до кнопки сохранить
        self.offer_page.scrol_up()                                                  # Скролл вверх
        # Заполнение анкеты
        self.offer_page.click_search_marka()                                        # Выпадающий список марок
        self.offer_page.click_select_marka()                                        # Выбор марки
        self.offer_page.click_search_model()                                        # Выпадающий список модели
        self.offer_page.click_select_model()                                        # Выбор модели
        self.offer_page.click_search_cuzov()                                        # Выпадающий список кузовов
        self.offer_page.click_select_cuzov()                                        # Выбор кузова
        self.offer_page.enter_color('Синий')                                        # Ввод цвета
        self.offer_page.enter_vin('VIN777C37')                                      # Ввод вин номера
        self.offer_page.enter_equipment('SE')                                       # Ввод комплектации
        self.offer_page.click_search_date()                                         # Выпадающий список дат
        self.offer_page.click_select_date()                                         # Выбор даты
        self.offer_page.scrol_down()                                                # Скролл ниже
        self.offer_page.enter_price('2249999')                                      # Ввод цены
        self.offer_page.enter_mileage('80100')                                      # Ввод пробега
        self.offer_page.click_search_transmission()                                 # Выпадающий список трансмиссии
        self.offer_page.click_select_transmission()                                 # Выбор трансмиссии
        self.offer_page.click_search_engine_capacity()                              # Выпадающий список объёма двигателя
        self.offer_page.click_select_engine_capacity()                              # Выбор объёма двигателя
        self.offer_page.click_search_engine_type()                                  # Выпадающий список типа двигателя
        self.offer_page.click_select_engine_type()                                  # Выбор типа двигателя
        self.offer_page.click_search_drive_unit()                                   # Выпадающий список привода
        self.offer_page.click_select_drive_unit()                                   # Выбор привода
        self.offer_page.click_search_state()                                        # Выпадающий список состояния
        self.offer_page.click_select_state()                                        # Выбор состояни
        self.offer_page.scrol_down()                                                # Скролл ниже
        self.offer_page.enter_horsepower('203')                                     # Ввод л.с
        self.offer_page.click_search_pts()                                          # Выпадающий список птс
        self.offer_page.click_select_pts()                                          # Выбор птс
        self.offer_page.enter_owners('1')                                           # Ввод кол-ва хозяев
        self.offer_page.click_search_accounting()                                   # Выпадающий список учета
        self.offer_page.click_select_accounting()                                   # Ввыбор учета
        self.offer_page.enter_telephone('79010334445')                              # Ввод номера телефона
        self.offer_page.scrol_down()                                                # Скролл ниже
        self.offer_page.photo_1()                                                   # Вставка фото 1
        self.offer_page.photo_2()                                                   # Вставка фото 2
        self.offer_page.photo_3()                                                   # Вставка фото 3
        self.offer_page.enter_description('Отличная тачка')                         # Ввод описания
        self.offer_page.save_button()                                               # Кнопка схранить
            # ДОБАВЛЕНИЕ АВТО НА САЙТ ЧЕРЕЗ АДМИНКУ
        # Cайт
        self.search.open()                                                          # Открытие каталога
        self.search.scrol_down_button()                                             # Скроол до кнопку сед. стр.
        self.search.next_page()                                                     # Следующая страница
        # admin
        self.admin_page.open()                                                      # Открытие админки
        self.admin_page.enter_login(self.data.LOGIN)                                # Ввод логина
        self.admin_page.enter_password(self.data.PASSWORD)                          # Ввод пароля
        self.admin_page.click_submit_button()                                       # Кнопка вход
        self.admin_page.car_button()                                                # Открыте вкладки автомобили
        self.admin_page.checkbox_click_settings_on_1()                              # Выбор авто 1
        self.admin_page.checkbox_click_settings_on_2()                              # Выбор авто 2
        self.admin_page.click_settings_select()                                     # Открытие настроек
        self.admin_page.click_settings()                                            # Выбор удаление авто
        self.admin_page.click_settings_button()                                     # Кнопка выбора
        self.admin_page.click_settings_button_agreement()                           # Подтверждение удаления авто
        self.admin_page.checkbox_click_on()                                         # Выбор чекбокса В продаже
        self.admin_page.checkbox_click_off()                                        # Отключение чекбокса В продаже
        self.admin_page.scrol_down()                                                # Скролл вниз
        self.admin_page.save_button()                                               # Сохранение изменений
        # Сайт
        self.search.open()                                                          # Открытие сайта
        self.search.scrol_down_button()                                             # Скрол до кнопки след. стр.
        self.search.next_page()                                                     # Следующая страница
        self.search.car_card_2()                                                    # Открытие добавленого авто
        self.search.scrol_down()                                                    # Скролл в карточке авто вниз
        self.search.scrol_up()                                                      # Скролл в карточке авто вверх
