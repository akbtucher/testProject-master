import allure

from pages.base_page import BasePage
from locators.locators import SearchPageLocators, CategoryPageLocators, SelectedCategoryLocators


@allure.title('Страница поиска')
class SearchPage(BasePage):

    with allure.step('Выбор сервиса "Картинки"'):
        def select_images_services(self):
            self.element_is_visible(SearchPageLocators.ALL_SERVICES).click()
            self.element_is_visible(SearchPageLocators.IMAGES_SERVICE).click()

    with allure.step('Метод проверки отображения поля поиска на странице'):
        def search_field_is_present(self):
            return "search field is present" if self.element_is_visible(SearchPageLocators.SEARCH_FIELD) is not None \
                else "search field is not present"

    with allure.step('Метод проверки отображения сервиса "Картинки" на странице'):
        def image_service_is_present(self):
            return "image service is present" if self.element_is_visible(SearchPageLocators.SEARCH_FIELD) is not None \
                else "image service is not present"


@allure.title('Страница выбора категорий')
class CategoryPage(BasePage):

    with allure.step('Метод выбора случайной категории и возврата результата выбора'):
        def select_random_category(self):
            selected_categories = self.element_is_visible(CategoryPageLocators.CATEGORIES)
            selected_categories.click()
            return selected_categories.get_attribute("data-grid-text")


@allure.title('Страница выбранной категории')
class SelectedCategoryPage(BasePage):

    with allure.step('Метод возврата результата выбранной категории'):
        def get_selected_value(self):
            result = self.element_is_visible(SelectedCategoryLocators.SEARCH_FIELD_SELECTED_CATEGORY)
            return result.get_attribute("value")
