'''
Created on Aug 25, 2011

@author: fairul.fahrurazi
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

	
 
		
		
	

