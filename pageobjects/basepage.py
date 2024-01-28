import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

TIMEOUT = 10


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def wait_for_seconds(seconds: int):
        time.sleep(seconds)

    def find_element(self, locator: tuple, timeout=TIMEOUT) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator: tuple, timeout=TIMEOUT) -> list[WebElement]:
        try:
            return WebDriverWait(self._driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except ValueError:
            return []

    def click(self, locator: tuple):
        self.find_element(locator).click()

    def send_keys(self, locator: tuple, text: str):
        self.find_element(locator).send_keys(text)

    # def print_text(self, text: str):
    #     actions = ActionChains(self._driver)
    #     for char in text:
    #         actions.send_keys(char)
    #     # actions.send_keys(Keys.ENTER)
    #     actions.perform()

    def select_by_visible_text(self, locator: tuple, value: str):
        select = Select(self.find_element(locator))
        select.select_by_visible_text(value)
        # self._driver.se



