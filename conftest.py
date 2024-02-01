import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=600,980")
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()
