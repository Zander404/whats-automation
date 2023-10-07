
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

def mensagem_direta(name:str, msg: str):
    ini = t.time()

    
    while True:
        
        try:
            wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_path)))

            search_box = driver.find_element(By.XPATH, search_box_path)
            search_box.send_keys(name)

            wait_component.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listitem']//span[@title='{name}']"))).click()

            wait_component.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
            message_box = driver.find_element(By.XPATH, message_box_path)
            message_box.send_keys(msg)
            fim = t.time()
            message_box.send_keys(fim-ini)
            message_box.send_keys(Keys.ENTER)
            sleep(1)
        
            break
        
        except Exception as e:
            raise e
        
        


def message_user(user:int, msg):
    ini = t.time()
    driver.get(f'https://web.whatsapp.com/send?phone={user}')
    wait_component.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    message_box = driver.find_element(By.XPATH, message_box_path)
    message_box.send_keys(msg)
    fim = t.time()
    message_box.send_keys(fim-ini)
    message_box.send_keys(Keys.ENTER)
    sleep(1)

    
def lista_de_contatos():
    import pandas as pd
    ini = t.time()
    i = 0
    numeros = pd.read_csv('teste.csv')
    for numero in numeros['telefone']:
        message_user(numero, numeros['mensagem'][i])
        i += 1
    fim = t.time()
    print(f"Demorou: {fim-ini}")


def close():
    driver.close()



# mensagem_direta("Crias LTDA", f" Demorou: ")

lista_de_contatos()

# message_user(5562992383814, "Demorou: ")
