from selenium.webdriver.common.by import By



class Signup:
    Nam="//input[@placeholder='Name']"
    Emailaddress="//input[@data-qa='signup-email']"
    Click_sign="//button[@data-qa='signup-button']"
    exist_email="//p[normalize-space()='Email Address already exist!']"

    def __init__(self, driver):
        self.driver = driver

    def Names(self, name):
        self.driver.find_element(By.XPATH, self.Nam).send_keys(name)

    def Email(self, name):
        self.driver.find_element(By.XPATH, self.Emailaddress).send_keys(name)

    def Click(self):
        self.driver.find_element(By.XPATH, self.Click_sign).click()
    def Exist_email(self):
        error= self.driver.find_element(By.XPATH, self.exist_email).text
        return error

class Account:
    Email="//input[@data-qa='login-email']"
    Password="Password"

    def __init__(self, driver):
        self.driver = driver

    def email(self,name):
        self.driver.find_elements(By.XPATH,self.Email).send_keys(name)

    def password(self,name):
        self.driver.find_elements(By.NAME,self.Password).send_keys(name)