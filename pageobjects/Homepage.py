from selenium.webdriver.common.by import By

class Home:

    myaccount = "//span[normalize-space()='My Account']"
    register = "//ul[@class='dropdown-menu dropdown-menu-right show']/li[1]"
    login = "//ul[@class='dropdown-menu dropdown-menu-right show']/li[2]"

    def __init__(self,driver):
        self.driver=driver

    def account(self):
        self.driver.find_element(By.XPATH,self.myaccount).click()

    def registers(self):
        self.driver.find_element(By.XPATH, self.register).click()

    def logins(self):
        self.driver.find_element(By.XPATH, self.login).click()