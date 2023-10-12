from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

service = Service(ChromeDriverManager().install())

dir_path = os.getcwd()


profile = os.path.join(dir_path, 'profile', 'wpp')

option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir={}".format(profile))
# option.add_argument("--headless=new")

driver = webdriver.Chrome(service=service, options=option)
wait_component = WebDriverWait(driver, 30)