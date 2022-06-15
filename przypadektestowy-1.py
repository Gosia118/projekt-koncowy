#IMPORT BIBLIOTEK
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#DANE TESTOWE UZYTKOWNIKA
my_email = "aaa@jigdrsrs.com"
my_password = "AAApass567"

class ProjectLogOut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_log_out_from_website(self):
        driver = self.driver
        sign_in = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in.click()

        registered_email = driver.find_element(By.ID, "email")
        registered_email.send_keys(my_email)

        registered_password = driver.find_element(By.ID, "passwd")
        registered_password.send_keys(my_password)

        sign_in_button = driver.find_element(By.ID, "SubmitLogin")
        sign_in_button.click()

        sleep(5)

        sign_out = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign out")
        sign_out.click()

        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
