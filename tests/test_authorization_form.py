import allure
import data.consts as consts
from pageobjects.authorization_page import AuthorizationPage
from pageobjects.thanks_modal import ThanksModal


@allure.suite("Practicum Test Suite")
@allure.title("Practicum Test Case")
def test_authorization_form(driver):
    with allure.step("Перейти на страницу 'automation-practice-form'"):
        page = AuthorizationPage(driver)
        modal = ThanksModal(driver)
        page.navigate()

    with allure.step("1 Заполнить поле First Name"):
        page.send_keys(page.input_first_name, consts.FIRST_NAME)

    with allure.step("2 Заполнить поле Last Name"):
        page.send_keys(page.input_last_name, consts.LAST_NAME)

    with allure.step("3 Заполнить поле Email"):
        page.send_keys(page.input_user_email, consts.EMAIL)

    with allure.step("4 Выбрать значение в Gender"):
        page.click(page.label_female)

    with allure.step("5 Заполнить поле Mobile"):
        page.send_keys(page.input_user_number, consts.USER_NUMBER)

    with allure.step("6 Заполнить поле Date of birth"):
        page.fill_in_datepicker(consts.DAY, consts.MONTH, consts.YEAR)

    with allure.step("7 Заполнить поле Subjects произвольной строкой"):
        page.fill_in_subjects_field(consts.SUBJ_ENGLISH)

    with allure.step("8 Загрузить изображение в поле Picture"):
        page.upload_test_picture()

    with allure.step("9 Заполнить поле Current Address"):
        page.send_keys(page.text_current_address, consts.CURRENT_ADDRESS)

    with allure.step("10 Выбрать любое значение в Select State"):
        STATE = page.div_select_by_index(page.div_state, 1)

    with allure.step("11 Выбрать любое значение в Select City"):
        CITY = page.div_select_by_index(page.div_city, 1)

    with allure.step("12 Нажать кнопку Submit"):
        page.click(page.button_submit)

    with allure.step("Проверка: Появилось всплывающее окно Thanks"):
        modal.expect_is_visible()

    with allure.step("Проверка: В таблице отображаются введенные значения"):
        modal.expect_fields_in_table(STATE, CITY)
