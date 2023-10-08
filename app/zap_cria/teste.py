from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time as t

from selenium.webdriver.support import expected_conditions as EC


global driver
global wait_component

from utils.paths import *
from utils.selenium_config import option, service, driver, wait_component

driver.get("https://web.whatsapp.com")

wait_component.until(EC.presence_of_element_located((By.XPATH, init_path)))


# def image_contato(name: int, file: any):
#     from  PIL import Image
#     import os
#     image_path = os.path.join(file)
#     image = Image.open(file)

#     while True:
#             wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
#             search_box = driver.find_element(By.XPATH, search_box_path)
#             search_box.send_keys(name)

#             wait_component.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listitem']//span[@title='{name}']"))).click()
#             wait_component.until(EC.element_to_be_clickable((By.XPATH, image_path))).click()





#     print(image)


# image_contato("Trabalhos", "./teste.jpeg")

# def lista_de_contatos():
#     import pandas as pd
#     ini = t.time()
#     i = 0
#     numeros = pd.read_csv('teste.csv')
#     for numero in numeros['telefone']:
#         i += 1
#         send_message_unsaved_contact(numero, numeros['mensagem'][i])
#     fim = t.time()
#     print(f"Demorou: {fim-ini}")


# def close():
#     driver.close()







