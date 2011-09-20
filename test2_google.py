from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import functionR


class Test2Google(unittest.TestCase):
    def setUp(self):
		functionR.setUp(self)
		
		
    def test_2_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("fairul rizal")
        driver.find_element_by_link_text("Fairul Rizal - Malaysia | LinkedIn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
