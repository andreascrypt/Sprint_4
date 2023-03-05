import allure
from page_objects.main_page import MainPage


class TestMainPage:

    @allure.description('По клику на логотип "Яндекс" в новом окне открывается главная Яндекса')
    @allure.title('Клик на лого "Яндекс"')
    def test_yandex_logo_click(self, browser):
        main_page = MainPage(browser)
        browser.get("https://qa-scooter.praktikum-services.ru/")
        main_page.yandex_logo_click()
        assert len(browser.window_handles) == 2

    @allure.description('При нажатии на логотип "Самокат" переход на главную страницу Самокат')
    @allure.title('Клик по лого "Самокат"')
    def test_click_samokat_logo(self, browser):
        main_page = MainPage(browser)
        browser.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.scooter_logo_click()
        assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"







