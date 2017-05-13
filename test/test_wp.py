import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

valid_login = "testerwsb_t1"
valid_pass = "adam1234"
invalid_login = "bleble"
invalid_pass = "bleble"

class WsbPLCheck2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_1(self):
        driver = self.driver
        driver.get("http://www.wp.pl/static.html")
        enter = driver.find_element_by_class_name("_22eBg")
        enter.click()
        login = driver.find_element_by_id("login")
        login.send_keys(valid_login)
        password = driver.find_element_by_id("password")
        password.send_keys(valid_pass)
        button1 = driver.find_element_by_id("btnSubmit")
        button1.click()
        odebrane = driver.find_element_by_link_text("Odebrane")
        odebrane.click()

    def test_2(self):
        driver = self.driver
        driver.get("http://www.wp.pl/static.html")
        enter = driver.find_element_by_class_name("_22eBg")
        enter.click()
        login = driver.find_element_by_id("login")
        login.send_keys(invalid_login)
        password = driver.find_element_by_id("password")
        password.send_keys(valid_pass)
        button1 = driver.find_element_by_id("btnSubmit")
        button1.click()
        odebrane = driver.find_element_by_link_text("Odebrane")
        odebrane.click()

    def test_3(self):
        driver = self.driver
        driver.get("http://www.wp.pl/static.html")
        enter = driver.find_element_by_class_name("_22eBg")
        enter.click()
        login = driver.find_element_by_id("login")
        login.send_keys(valid_login)
        password = driver.find_element_by_id("password")
        password.send_keys(invalid_pass)
        button1 = driver.find_element_by_id("btnSubmit")
        button1.click()
        odebrane = driver.find_element_by_link_text("Odebrane")
        odebrane.click()

    def test_4(self):
        driver = self.driver
        driver.get("http://www.wp.pl/static.html")
        enter = driver.find_element_by_class_name("_22eBg")
        enter.click()
        login = driver.find_element_by_id("login")
        login.send_keys(invalid_login)
        password = driver.find_element_by_id("password")
        password.send_keys(invalid_pass)
        button1 = driver.find_element_by_id("btnSubmit")
        button1.click()
        odebrane = driver.find_element_by_link_text("Odebrane")
        odebrane.click()


    def tearDown(self):
        self.driver.find_element_by_link_text("wyloguj").click()
        self.driver.quit()

if __name__ == "__main__":
  unittest.main(verbosity=2)
