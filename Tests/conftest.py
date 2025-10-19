import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {user_language}..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with language: {user_language}..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        options = FirefoxOptions()
        browser = webdriver.Firefox(firefox_profile=fp, options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
    # browser.close()