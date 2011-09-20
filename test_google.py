'''
Created on Aug 25, 2011

@author: fairul.fahrurazi
This is just an example of selenium 2.0 test cases python based for reference .. 
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest
#You need to import functionR.py file as at least setUp function is located there .If you think any functions that will be hevily used,
#it's a good thing to define in  functionR.py file ,so a test case can just call it to re-use it .
import functionR


#Specify Your pre-Test Case title as part of the class    
class GoogleSearchJohnLennon(unittest.TestCase):
         
#Dont change setUp over here.If needed to change ,do it at function.py -setup method.
            def setUp(self):
                functionR.setUp(self)
               
################ Your Selenium 2..0/webdriver Python test cases should start here ,Below is the example#############################
            def test_google_search_john_lennon(self):
                driver = self.driver
                driver.get("http://www.google.com.my/")
                driver.find_element_by_id("lst-ib").clear()
                driver.find_element_by_id("lst-ib").send_keys("John Lennon")
                driver.find_element_by_css_selector("#imagebox_bigimages > h3.r > a > em").click()
            
    
            def is_element_present(self, how, what):
                try: self.driver.find_element(by=how, value=what)
                except NoSuchElementException, e: return False
                return True
   
            def tearDown(self):
                self.driver.quit()
                self.assertEqual([], self.verificationErrors)
################Test Case completed###########################################

if __name__ == "__main__":
            unittest.main()
            


    
    
    
