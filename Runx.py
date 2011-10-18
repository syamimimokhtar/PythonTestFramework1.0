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
import os
import nose
import re
from ConfigParser import SafeConfigParser

#Read test browsers needed for test in config.ini
parser = SafeConfigParser()
parser.read('config.ini')
browser=parser.get('Selenium_Config','browser')
list=browser.split(',')

#Read testReport pre-fix name in config.ini.
testReport=parser.get('Selenium_Config','testResult')


for i in list:
  o = open("output","w")
  data = open("functionR.py").read()
  o.write( re.sub(r'\bbrowserjz1\b',"'"+i+"'",data)  )
  o.close()
  os.remove("functionR.py")
  os.rename("output","functionR.py")
  os.system("nosetests --with-xunit")
  os.rename("nosetests.xml",testReport+"_for_"+i+".xml")
  o = open("output","w")
  data = open("functionR.py").read()
  o.write( re.sub("'"+i+"'","browserjz1",data)  )
  o.close()
  os.remove("functionR.py")
  os.rename("output","functionR.py")

	
 
		
		
	

