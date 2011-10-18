'''
Created on Aug 25, 2011
Copyright 2011 mimos-selenium2.0-pythonTestFramework1.0 Developers
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
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