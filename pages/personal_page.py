# import time
#
# import allure
# from base.base_page import BasePage
# from config.links import Links
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Keys
#
# class PersonalPage(BasePage):                                       # локатор для работы на этой странице
#
#     PAGE_URL = Links.PERSONAL_PAGE
#
#     FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")      # локатор поля
#     SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")        # локатор кнопки
#     SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")      # локатор спинера-загрузки
#
    # def change_name(self, new_name):                                # для смены текста в поле
    #     with allure.step(f"Change name on '{new_name}'"):           # для алюра
    #         first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))   #
    #         first_name_field.send_keys(Keys.COMMAND + "A")          # очистка поля
    #         first_name_field.send_keys(Keys.BACKSPACE)              # очестка поля
    #         first_name_field.send_keys(new_name)                    # новый текст
    #         self.name = new_name                                    # новый текст
#
#     @allure.step("Save changes")                                    # для алюра
#     def save_changes(self):                                         # сохраняем по кнопке
#         self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()   #
#
#     @allure.step("Changes has been saved successfuly")              # для алюра
#     def is_changes_saved(self):                                     # проверка изменений на сохранение
#         self.wait.until(EC.invisibility_of_element_located(self.SPINNER))   #
#         self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))    #
#         self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))   # ждём что в поле изменилось значение на наш текст