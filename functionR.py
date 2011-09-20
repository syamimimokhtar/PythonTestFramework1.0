from selenium import webdriver
from ConfigParser import SafeConfigParser
#import Run

#Read configuration parameter from config.ini
parser = SafeConfigParser()
parser.read('config.ini')
seleniumHubserver = parser.get('Selenium_Config', 'seleniumHubserver')
port = parser.get('Selenium_Config', 'port')
url = parser.get('Selenium_Config','base_url')

browserjz= browserjz1



def setUp(self):
        self.driver = webdriver.Remote(
                                       command_executor='http://'+ seleniumHubserver +':'+ port +'/wd/hub',
                                       desired_capabilities={'browserName': browserjz})
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
		
		
#You should be able to add any functions you need  below ###