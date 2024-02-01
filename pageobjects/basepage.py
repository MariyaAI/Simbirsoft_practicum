import time
from allure import step
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

TIMEOUT = 10


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    @step("wait_for_seconds")
    def wait_for_seconds(seconds: int):
        time.sleep(seconds)

    @step("find_element")
    def find_element(self, locator: tuple, timeout=TIMEOUT) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @step("find_elements")
    def find_elements(self, locator: tuple, timeout=TIMEOUT) -> list[WebElement]:
        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except ValueError:
            return []

    @step("click")
    def click(self, locator: tuple):
        self.find_element(locator).click()

    @step("send_keys")
    def send_keys(self, locator: tuple, text: str):
        self.find_element(locator).send_keys(text)

    @step("select_by_visible_text")
    def select_by_visible_text(self, locator: tuple, value: str):
        select = Select(self.find_element(locator))
        select.select_by_visible_text(value)

    def scroll_to_element(self, locator: tuple):
        e = self.find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", e)
