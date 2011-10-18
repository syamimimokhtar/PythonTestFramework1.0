# Readme  

This is basically the selenium 2.0 python test case framework .This an attempt to provide the following features  

1. consolidates all selenium 2.0 python test case and run them using a nosetests against a configurable parameters  
    * Browsers type Ð IE and Firefox and Chrome etc  
    * Selenium Hub Server  
    * Selenium Hub Server Port  
    * Base URL
    * Test Report filename in Junit xml format  

2.  Running all test case in parallel per browser using nosetests multiprocessing feature. *Note there is a work in progress to fix running test cases in parallel regardless of browser type, as of now the implementation is - test cases will run in parallel for one type of browser first  i.e Firefox before moving to the next browser type or version.  

3.  Provide a Junit xml report . 

# Link to wiki  
**[How to Install] (https://github.com/fairul82/PythonTestFramework1.0/wiki/How-to-Install)** 
**[Getting Started] (https://github.com/fairul82/PythonTestFramework1.0/wiki/Getting-Started)**   
**[How to Setup Environment] (https://github.com/fairul82/PythonTestFramework1.0/wiki/How-to-Setup-Environment)** 
**[How to Run] (https://github.com/fairul82/PythonTestFramework1.0/wiki/How-to-Run)** 


