import allure

from pages.yandex_pages import SearchPage, CategoryPage, SelectedCategoryPage


@allure.suite("Pages")
class TestPages:

    @allure.feature("Тестовое задание: 'Первый сценарий'")
    def test_pages(self, driver):

        page = SearchPage(driver, 'https://ya.ru/')

        with allure.step('Открытие главной страницы Яндекса'):
            page.open()

        with allure.step('Проверка, что присутствует поле поиска'):
            page.search_field_is_present()

        with allure.step('Проверка, что присутствует кнопка перехода в раздел "Картинки"'):
            page.image_service_is_present()

        with allure.step('Выбор раздела "Картинки"'):
            page.select_images_services()

        with allure.step('Переключение на новое окно браузера'):
            driver.switch_to.window(driver.window_handles[1])

        with allure.step('Проверка адреса страницы, который должен быть или начинаться на "https://yandex.ru/images/"'):
            assert driver.current_url.startswith("https://yandex.ru/images/"), "Wrong page address"

        with allure.step('Случайный выбор категории'):
            page = CategoryPage(driver, 'https://yandex.ru/images/')
            result = page.select_random_category()

        with allure.step('Проверка текста в поле поиска, который должен совпадать с названием категории'):
            page = SelectedCategoryPage(driver, driver.current_url)
            assert page.get_selected_value() == result, \
                "The text in the search field must match the name of the category"





