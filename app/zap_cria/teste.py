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


def send_message(message:str) -> None:
    try:
        wait_component.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
        message_box = driver.find_element(By.XPATH, message_box_path)
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        sleep(1)
    except Exception as e:
        return {"response": f"Erro no Envio da Mensagem: {e}"}
    

def search_unsave_contact(number: int) -> object:
    try:
        wait_component.until(EC.element_to_be_clickable((By.XPATH, new_chat_path))).click()
        wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_unsave_chat_path)))
        search_box_new_chat = driver.find_element(By.XPATH, search_box_unsave_chat_path)
        search_box_new_chat.send_keys(number)
        sleep(0.2)
        if(wait_component.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div/div/div/div[1]/div/div[2]')))):
            wait_component.until(EC.presence_of_element_located((By.XPATH, unsave_contact_path)))
            sleep(0.2)
            wait_component.until(EC.element_to_be_clickable((By.XPATH, unsave_contact_path))).click()
        else:
            wait_component.until(EC.presence_of_element_located((By.XPATH, save_contact_path)))
            sleep(0.2)
            wait_component.until(EC.element_to_be_clickable((By.XPATH, save_contact_path))).click()

    except Exception as e:
        return {"response": f"Erro na procura do contato: {e}"}

def search_save_contact(number: int) -> object:
    try:
        wait_component.until(EC.element_to_be_clickable((By.XPATH, new_chat_path))).click()
        wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_unsave_chat_path)))
        search_box_new_chat = driver.find_element(By.XPATH, search_box_unsave_chat_path)
        search_box_new_chat.send_keys(number)
        wait_component.until(EC.presence_of_element_located((By.XPATH, save_contact_path)))
        sleep(0.2)
        wait_component.until(EC.element_to_be_clickable((By.XPATH, save_contact_path))).click()
    except Exception as e:
        return {"response": f"Erro na procura do contato: {e}"}        

def send_message_unsaved_contact(number:int, message:str) -> object:
    try:
        # Procurar contato
        search_unsave_contact(number)

        # Transforma em função
        send_message(message=message)
        response = {"response": "Mensagem enviada com sucesso"}

    except Exception as e:
        response = {"response": f"Mensagem não enviada: {e}"}

    finally:
        return response


def send_message_saved_contact(number:int, message:str) -> object:
    try:
        # Procurar contato
        search_save_contact(number)

        # Transforma em função
        send_message(message=message)
        response = {"response": "Mensagem enviada com sucesso"}

    except Exception as e:
        response = {"response": f"Mensagem não enviada: {e}"}

    finally:
        return response



def bulk_message(list: list, message: str):

    import pandas as pd
    i = 0
    numeros = pd.read_csv(list)
    for numero in numeros['number']:
        i += 1
        send_message_saved_contact(numero, message)



bulk_message("teste.csv", "ola")