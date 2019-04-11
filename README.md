<h3>Hi everyone! This is my little Revoo testing project 
I will try to explain my logic in this brief document.</h3>

  
<h4>My technology steck is: </h4>
 - Python with Pytest and UnitTest
 - Selenium with Webdriver (headless and not)
 - Page Object Pattern. Good for Ui tests
 - Allure Report for Reporting

<h4>What we are testing:</h4>

Product page with Reevoo modules. I found that we user similar modules (Customer Reviews, Ask Owner, Question) in several places. So We should not tests them all, its enough to tests them.
That is why I chouse Rating Reviews popup.

<h4>Test cases</h4>
This is just an example of what might be tested. 
 - Test if rating element located on the screen
 - Test if rating values returned
 - Test if it is possible to open popup by clicking on the 'icon'
 - Test if ratings and reviews data correct and comply with data on the Product page
 - Test scores calculation
 - Test if all elements visible 

What also might be tested:
 - Lunch tests on differed screens and resolutions
 - Lunch with differed browsers
 - It is possible to test layout problems. But they should be specified. 

<h4>Testing results</h4>
All my tests are PASSED
Test report example page
Some screens
Demo life report presentation

<h4>How to lunch test on your localhost</h4>

use *nix
install python3:
```bash
# Install python
sudo apt-get install python3
sudo apt-get install python3-pip

# Install Alure
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure

# Open project folder
pip install -r requirements.txt
# lunch tests from /
pytest tests/ --alluredir=reports/ -s -v

# After test committed 
allure serve /home/path/to/project/target/surefire-reports/
```
Allure Demo report example 
[here](https://demo.qameta.io/allure/)
