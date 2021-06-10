from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random
import pytest
import config
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture for browser selection and browser launching
    """
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--no-sandbox')
        # options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.get(url=config.CROP_MONITORING_URL)
        time.sleep(2)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument('--no-sandbox')
        # options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument("--incognito")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.get(url=config.CROP_MONITORING_URL)
        time.sleep(2)

    else:
        print(f"Browser <browser_name> is still not implemented")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def generate_login():
    login = config.MAIL.split("@")
    login = f'{login[0]}+{str(random.randrange(99999))}@{login[1]}'
    print(login)
    yield login
