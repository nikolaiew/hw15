import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()


def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is 'headless' mode, but you can set --browser_mode='headless'")
    parser.addoption('--browser_window_size', action='store', default="maximized",
                     help="By default is 'maximized' mode, but you can set --browser_window_size='1280'")


@pytest.fixture(scope="function")
def browser(request):
    print("\n>>> start browser for test...")

#  Обробка параметризації режиму браузера (headless/gui)
    browser_mode = request.config.getoption("browser_mode")
    if browser_mode == "gui":
        print(f"browser_mode: {browser_mode}")
    elif browser_mode == "headless":
        options.add_argument('--headless')
        print(f"browser_mode: {browser_mode}")
    else:
        print("Режим запуску браузера повинен бути або 'gui' або 'headless'")

#  Обробка параметризації розміру вікна браузера (maximized/1280)
    browser_window_size = request.config.getoption("browser_window_size")
    if browser_window_size == "maximized":
        options.add_argument('--start-maximized')
        print(f"browser_window_size: {browser_window_size}")
    elif browser_window_size == "1280":
        options.add_argument('--window-size=1280,800')
        print(f"browser_window_size: {browser_window_size}")
    else:
        print("Розмір вікна браузера повинен бути або 'maximized' або '1280'")

    browser = webdriver.Chrome(options=options)
    yield browser
    print("<<< ... quit browser\n==========================")
    browser.quit()

