from utils.selenium_config import option, service, driver, wait_component
from utils.paths import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time as t

from selenium.webdriver.support import expected_conditions as EC


global driver
global wait_component

driver.get("https://web.whatsapp.com")

wait_component.until(EC.presence_of_element_located((By.XPATH, init_path)))



# def lista_de_contatos(lista: list, message: str):

#     import pandas as pd
#     i = 0
#     numeros = pd.read_csv(lista)
#     for numero in numeros['telefone']:
#         i += 1
#         send_message_unsaved_contact(numero, message)
