from selenium.webdriver.common.by import By
import data.consts as consts
from pageobjects.basepage import BasePage


class ThanksModal(BasePage):
    div_title = (By.XPATH, "//*[@id='example-modal-sizes-title-lg']")
    td_student_name = (By.XPATH, "//td[.='Student Name']/following-sibling::td")
    td_student_email = (By.XPATH, "//td[.='Student Email']/following-sibling::td")
    td_gender = (By.XPATH, "//td[.='Gender']/following-sibling::td")
    td_mobile = (By.XPATH, "//td[.='Mobile']/following-sibling::td")
    td_date_of_birth = (By.XPATH, "//td[.='Date of Birth']/following-sibling::td")
    td_subjects = (By.XPATH, "//td[.='Subjects']/following-sibling::td")
    td_picture = (By.XPATH, "//td[.='Picture']/following-sibling::td")
    td_address = (By.XPATH, "//td[.='Address']/following-sibling::td")
    td_state_and_city = (By.XPATH, "//td[.='State and City']/following-sibling::td")

    def expect_is_visible(self):
        assert self.find_element(
            self.div_title
        ), "Модалка(поиск по тайтлу) не отображается"

    def expect_fields_in_table(self, state: str, city: str):
        assert consts.FIRST_NAME in self.find_element(self.td_student_name).text
        assert consts.LAST_NAME in self.find_element(self.td_student_name).text

        assert consts.EMAIL in self.find_element(self.td_student_email).text
        assert consts.GENDER in self.find_element(self.td_gender).text
        assert consts.USER_NUMBER in self.find_element(self.td_mobile).text

        assert consts.DAY in self.find_element(self.td_date_of_birth).text
        assert consts.MONTH[:3] in self.find_element(self.td_date_of_birth).text
        assert consts.YEAR in self.find_element(self.td_date_of_birth).text

        assert consts.SUBJ_ENGLISH in self.find_element(self.td_subjects).text
        assert consts.CURRENT_ADDRESS in self.find_element(self.td_address).text

        assert state in self.find_element(self.td_state_and_city).text
        assert city in self.find_element(self.td_state_and_city).text
