# conftest.py (расширенная версия)
import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr, etc.")
    parser.addoption('--headless', action='store_true', default=False,
                     help="Run tests in headless mode")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    is_headless = request.config.getoption("headless")
    browser = None

    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {user_language}..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        if is_headless:
            options.add_argument("--headless")

        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with language: {user_language}..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        if is_headless:
            options.add_argument("--headless")

        browser = webdriver.Firefox(firefox_profile=fp, options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def wait(browser):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(browser, 10)


@pytest.fixture
def take_screenshot(browser):
    """Фикстура для создания скриншотов при падении тестов"""

    def _take_screenshot(test_name):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{int(time.time())}.png")
        browser.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    return _take_screenshot


@pytest.fixture
def page_loader(browser):
    """Фикстура для загрузки страниц с ожиданием"""

    def _load_page(url, timeout=10):
        browser.get(url)
        WebDriverWait(browser, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    return _load_page