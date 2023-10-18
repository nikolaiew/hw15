import pytest
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"


class TestPage1():
    @pytest.mark.header
    def test_is_button_search_on_the_main_page(self, browser):
        print("\nШукаємо кнопку пошуку")
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    @pytest.mark.header
    def test_is_wishlist_link_on_the_main_page(self, browser):
        print("\nШукаємо лінк на список бажань")
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='wish/show']")


    @pytest.mark.header
    def test_is_basket_link_on_the_main_page(self, browser):
        print("\nШукаємо лінк на корзину")
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")


    @pytest.mark.header
    def test_is_currency_dropdown_on_the_main_page(self, browser):
        print("\nШукаємо меню валюти")
        browser.get(link)
        browser.find_element(By.XPATH, "//select[@id='currency']")


    @pytest.mark.footer
    def test_is_logo_link_on_the_main_page(self, browser):
        print("\nШукаємо лого в футері")
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class='logo']/a")


    @pytest.mark.footer
    def test_is_telegram_link_on_the_main_page(self, browser):
        print("\nШукаємо telegram в футері")
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='https://t.me/casenik_com_ua']")

