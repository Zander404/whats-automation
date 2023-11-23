from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import os

service = Service(ChromeDriverManager().install())

dir_path = os.getcwd()


profile = os.path.join(dir_path, 'profile', 'wpp')

option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir={}".format(profile))
option.add_argument("--headless=new")

selenium_grid_url = "http://127.0.0.1:4444/wd/hub"

capabilities = DesiredCapabilities.CHROME.copy()

driver = webdriver.Remote(selenium_grid_url, capabilities, options=option)
wait_component = WebDriverWait(driver, 180)