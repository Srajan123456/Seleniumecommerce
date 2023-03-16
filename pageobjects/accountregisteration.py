from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Accounts:
    mr = "id_gender1"
    mrs = "id_gender2"
    name = "//input[@data-qa='name']"
    password = "password"
    day = "days"
    month = "months"
    year = "years"
    newsletter="newsletter"
    special_offer="optin"
    first_name="first_name"
    last_name="last_name"
    company="company"
    address="address1"
    address2="address2"
    country="country"
    state="state"
    city="city"
    zipcode="zipcode"
    mobile_no="mobile_number"
    click="//button[normalize-space()='Create Account']"
    verify_accountcreation="//b[normalize-space()='Account Created!']"

    title="//b[normalize-space()='Enter Account Information']"

    def __init__(self, driver):
        self.driver = driver

    def Mr(self):
        self.driver.find_element(By.ID, self.mr).click()

    def Mrs(self):
        self.driver.find_element(By.ID, self.mrs).click()

    def Name(self, enter_name):
        self.driver.find_element(By.XPATH, self.name).send_keys(enter_name)

    def Password(self, enter_password):
        self.driver.find_element(By.ID, self.password).send_keys(enter_password)

    def Days(self, da):
        datepicker_days = Select(self.driver.find_element(By.NAME, self.day))
        datepicker_days.select_by_visible_text(da)

    def Months(self, mon):
        datepicker_month = Select(self.driver.find_element(By.NAME, self.month))
        datepicker_month.select_by_visible_text(mon)

    def Years(self, yea):
        datepicker_year = Select(self.driver.find_element(By.NAME, self.year))
        datepicker_year.select_by_visible_text(yea)

    def Newsletter(self):
        self.driver.find_element(By.ID, self.newsletter).click()

    def Special_offer(self):
        self.driver.find_element(By.ID, self.special_offer).click()

    def First_name(self, name):
        self.driver.find_element(By.ID, self.first_name).send_keys(name)

    def Last_name(self ,name):
        self.driver.find_element(By.ID, self.last_name).send_keys(name)

    def Company(self ,name):
        self.driver.find_element(By.ID, self.company).send_keys(name)


    def Address(self, name):
        self.driver.find_element(By.ID, self.address).send_keys(name)

    def Address_2(self, name):
        self.driver.find_element(By.ID, self.address2).send_keys(name)

    def Country(self, country_name):
        pick_country = Select(self.driver.find_element(By.ID, self.country))
        pick_country.select_by_visible_text(country_name)

    def State(self, name):
        self.driver.find_element(By.ID, self.state).send_keys(name)

    def City(self, name):
        self.driver.find_element(By.ID, self.city).send_keys(name)

    def Zipcode(self, name):
        self.driver.find_element(By.ID, self.zipcode).send_keys(name)

    def Mobile_no(self, name):
        self.driver.find_element(By.ID, self.mobile_no).send_keys(name)

    def Create_account(self):
        self.driver.find_element(By.XPATH, self.click).click()

    def Title(self):
        page_title= self.driver.find_element(By.XPATH, self.title).text
        return page_title

    def Verify_accountcreation(self):
        verify_tittle= self.driver.find_element(By.XPATH, self.verify_accountcreation).text
        return verify_tittle












    # class Account:
#     firstnameid = "input-firstname"
#     lastnameid = "input-lastname"
#     emailid = "input-email"
#     passwordid = "input-password"
#     newsletteridyes="input-newsletter-yes"
#     newsletteridno="input-newsletter-no"
#     agreeclickname="agree"
#     continuebutton="//button[@class='btn btn-primary']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def Firstname(self, name):
#         self.driver.find_element(By.ID, self.firstnameid).send_keys(name)
#
#     def Lastname(self, name):
#         self.driver.find_element(By.ID, self.lastnameid).send_keys(name)
#
#     def Email(self, name):
#         self.driver.find_element(By.ID, self.emailid).send_keys(name)
#
#     def Password(self, name):
#         self.driver.find_element(By.ID, self.passwordid).send_keys(name)
#
#     def Newslateryes(self):
#         self.driver.find_element(By.ID, self.newsletteridyes).click()
#
#     def Newslaterno(self):
#         self.driver.find_element(By.ID, self.newsletteridno).click()
#
#     def Agree(self):
#         self.driver.find_element(By.NAME, self.agreeclickname).click()
#
#     def Continue(self):
#         self.driver.find_element(By.XPATH, self.continuebutton).click()
