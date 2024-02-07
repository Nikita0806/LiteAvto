import pytest
from config.data import Data
from pages.for_login.login_page import LoginPage
from pages.for_registration.registration_page import RegistrationPage
from pages.for_login.dashboard_login_page import DashboardLoginPage
from pages.for_registration.dashboard_registration_page import DashboardRegistrationPage
from pages.for_search.dashboard_search_page import SearchMarka
# from pages.personal_page import PersonalPage


class BaseTest:                             # базовый для наших тестов для инотации типов

    data: Data                              # из данных (пароли)

    login_page: LoginPage                   # аннотация
    registration_page: RegistrationPage                   # аннотация
    dashboard_login_page: DashboardLoginPage           # аннотация
    dashboard_registration_page: DashboardRegistrationPage           # аннотация
    search_marka: SearchMarka
    # personal_page: PersonalPage             # аннотация

    @pytest.fixture(autouse=True)           # autouse=True для всех тестов она применяется
    def setup(self, request, driver):       # фикстура
        request.cls.driver = driver         # чтобы в тестах могли использовать драйвер
        request.cls.data = Data()           # чтобы в тестах могли использовать пароли

        request.cls.login_page = LoginPage(driver)          # объекты страниц
        request.cls.registration_page = RegistrationPage(driver)          # объекты страниц
        request.cls.dashboard_login_page = DashboardLoginPage(driver)  # объекты страниц
        request.cls.dashboard_registration_page = DashboardRegistrationPage(driver)  # объекты страниц
        request.cls.search_marka = SearchMarka(driver)  # объекты страниц
        # request.cls.personal_page = PersonalPage(driver)    # объекты страниц