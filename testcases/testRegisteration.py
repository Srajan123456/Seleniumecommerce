import time

from pageobjects.Homepage import Home
class Test_Register:

    base_url = "https://demo.opencart.com/"

    def testRg(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.hp = Home(self.driver)
        self.hp.account()
        self.hp.registers()
        time.sleep(10)
        assert True == True