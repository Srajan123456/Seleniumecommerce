from selenium.webdriver.common.by import By

class Home:

    signup="//a[normalize-space()='Signup / Login']"
    product="//a[normalize-space()=' Products']"
    register="//ul[@class='dropdown-menu dropdown-menu-right show']/li[1]"
    login="//a[normalize-space()='Signup / Login']"
    cart="//a[normalize-space()=' Cart']"
    contact="//a[normalize-space()='Contact us']"

    def __init__(self,driver):
        self.driver=driver

    def signin(self):
        self.driver.find_element(By.XPATH,self.signup).click()

    def log(self):
        self.driver.find_element(By.XPATH,self.login).click()

    def products(self):
        self.driver.find_element(By.XPATH,self.product).click()

    def carts(self):
        self.driver.find_element(By.XPATH,self.cart).click()

    def contactus(self):
        self.driver.find_element(By.XPATH,self.contact).click()
























    # def products(self):
    #     self.driver.find_element(By.XPATH,self.product).click()
    #
    #
    # def registers(self):
    #     self.driver.find_element(By.XPATH, self.register).click()
    #
    # def logins(self):
    #     self.driver.find_element(By.XPATH, self.login).click()