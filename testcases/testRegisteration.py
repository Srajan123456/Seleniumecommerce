from utilities.customLogger import LogGen
from pageobjects.Homepage import Home
from pageobjects.signuploginpage import Signup
from pageobjects.accountregisteration import Accounts
import time
import datetime
class Test_Register:

    base_url ="https://automationexercise.com/"
    logger=LogGen.loggen()

    def testRg01(self, setup):
        #Validate Signup an Account
        self.logger.info("test start")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.signin()
        self.sign = Signup(self.driver)
        self.sign.Names("King")
        self.sign.Email("sr@gmail.com")
        self.sign.Click()
        self.reg = Accounts(self.driver)
        title= self.reg.Title()
        self.driver.save_screenshot("../screenshots/" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png")
        if 'Enter Account Information'==title:
            assert True == True
        else:
            assert False == False


    def testRg02(self, setup):
        #Validate Registering an Account by providing only mandatory field
        self.logger.info("test start")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.signin()
        self.sign = Signup(self.driver)
        self.sign.Names("King")
        self.sign.Email("sr@gmail.com")
        self.sign.Click()
        self.reg = Accounts(self.driver)
        self.reg.Password("123456")
        self.reg.First_name("Srajan")
        self.reg.Last_name("Gupta")
        self.reg.Address("chotibazar")
        self.reg.Country("Canada")
        self.reg.State("u.p")
        self.reg.City("Banda")
        self.reg.Zipcode("210001")
        self.reg.Mobile_no("8960653453")
        self.reg.Create_account()
        verify= self.reg.Verify_accountcreation()
        self.driver.save_screenshot("../screenshots/" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png")
        if 'Account Created!'==verify:
            assert True == True
        else:
            assert False == False

    def testRg03(self, setup):
        #Validate Registering an Account by providing all the fields
        self.logger.info("test start")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.signin()
        self.sign = Signup(self.driver)
        self.sign.Names("King")
        self.sign.Email("Killss@gmail.com")
        self.sign.Click()
        self.reg = Accounts(self.driver)
        self.reg.Password("123456")
        self.reg.Days("23")
        self.reg.Months("April")
        self.reg.Years("2000")
        time.sleep(10)
        self.reg.Newsletter()
        self.reg.Special_offer()
        self.reg.First_name("Srajan")
        self.reg.Last_name("Gupta")
        self.reg.Company("kinley")
        self.reg.Address("chotibazar")
        self.reg.Address_2("thatharai")
        self.reg.Country("Canada")
        self.reg.State("u.p")
        self.reg.City("Banda")
        self.reg.Zipcode("210001")
        self.reg.Mobile_no("8960653453")
        self.reg.Create_account()
        verify= self.reg.Verify_accountcreation()
        self.driver.save_screenshot("../screenshots/" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png")
        if 'Account Created!'==verify:
            assert True == True
        else:
            assert False == False


    def testRg04(self, setup):
        #Validate proper notification messages are displayed for the mandatory fields, when you don't provide any fields in the 'Register Account' page and submit
        self.logger.info("test start")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.signin()
        self.sign = Signup(self.driver)
        self.sign.Names("King")
        self.sign.Email("Kipss@gmail.com")
        self.sign.Click()
        self.reg = Accounts(self.driver)
        self.reg.Password("123456")
        self.reg.First_name("Srajan")
        self.reg.Last_name("Gupta")
        self.reg.Address("chotibazar")
        self.reg.Country("Canada")
        self.reg.State("u.p")
        self.reg.City("Banda")
        self.reg.Zipcode("210001")
        self.reg.Mobile_no("")
        self.reg.Create_account()
        self.driver.save_screenshot("../screenshots/" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png")
        title= self.reg.Title()
        if 'Enter Account Information'==title:
            assert True == True
        else:
            assert False == False

    def testRg05(self, setup):
        #Validate Registering an Account by providing the existing account details (i.e. existing email address)
        self.logger.info("test start")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.signin()
        self.sign = Signup(self.driver)
        self.sign.Names("King")
        self.sign.Email("Kills@gmail.com")
        self.sign.Click()
        error= self.sign.Exist_email()
        self.driver.save_screenshot("../screenshots/" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png")
        if error=="Email Address already exist!":
            assert True == True
        else:
            assert False == False
