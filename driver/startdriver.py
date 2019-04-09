import os
import platform
from selenium import webdriver

'''
Here we initialise basic WebDriver
We use Webdrivber 2.42, Chromedriver 
https://sites.google.com/a/chromium.org/chromedriver/downloads
DO NOT forget to update the webdriver

'''

'''
Webdriver initialization
If host is darwin - use Chromedirver for MAC
Else: host is linux, Chrome will be lunched under virtual display
'''


def select_driver():
    chrome_options = webdriver.ChromeOptions()

    # Start browser in incognito mode
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("user-data-dir=selenium")
    # Files downloading dir /common/files
    # download_dir = os.path.dirname(__file__).replace('webdriver', 'common/files')

    # Block Web App notifications
    prefs = {"profile.default_content_setting_values.notifications": 2,
             # "download.default_directory": download_dir,
             # "directory_upgrade": True,
             # "safebrowsing.enabled": True
             }
    chrome_options.add_experimental_option("prefs", prefs)

    # Find OS and select a Driver
    if str(platform.system()).lower() == 'darwin':
        driver_location = os.path.dirname(__file__) + '/chromedriver-mac'
    else:
        driver_location = os.path.dirname(__file__) + '/chromedriver-lin'

        # Lunch virtual display
        # display = Display(visible=0, size=(1024, 768))
        # display.start()

    # Basic driver settings, location and mode
    driver = webdriver.Chrome(executable_path=driver_location,
                              chrome_options=chrome_options, )

    return driver


class StartDriver(object):
    def __init__(self):
        self.driver = select_driver()

    def start(self):
        driver = self.driver
        return driver