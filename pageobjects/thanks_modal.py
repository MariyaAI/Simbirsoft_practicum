from pageobjects.basepage import BasePage


class ThanksModal(BasePage):
    div_title = "//*[@id='example-modal-sizes-title-lg']"
    td_student_name = "//td[.='Student Name']/following-sibling::td"
    td_student_email = "//td[.='Student Email']/following-sibling::td"
    td_gender = "//td[.='Gender']/following-sibling::td"
    td_mobile = "//td[.='Mobile']/following-sibling::td"
    td_date_of_birth = "//td[.='Date of Birth']/following-sibling::td"
    td_subjects = "//td[.='Subjects']/following-sibling::td"
    td_picture = "//td[.='Picture']/following-sibling::td"
    td_address = "//td[.='Address']/following-sibling::td"
    td_state_and_city = "//td[.='State and City']/following-sibling::td"


"""
Student Name	Maria Adoevskaia
Student Email	Adoevskaia@gmail.com
Gender	Female
Mobile	7909090990
Date of Birth	26 January,2024
Subjects	English
Hobbies	
Picture	1.png
Address	SAMARA
State and City	Uttar Pradesh Lucknow
"""
