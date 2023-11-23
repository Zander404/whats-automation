
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time as t
import os

from selenium.webdriver.support import expected_conditions as EC


global driver
global wait_component

from .utils.paths import *
from .utils.selenium_config import option, service, driver, wait_component

driver.get("https://web.whatsapp.com")

wait_component.until(EC.presence_of_element_located((By.XPATH, init_path)))


def send_message(message:str) -> object:
    try:
        wait_component.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
        message_box = driver.find_element(By.XPATH, message_box_path)
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        sleep(1)
    except Exception as e:
        return {"response": f"Erro no Envio da Mensagem: {e}"}
    

def search_contact(name: str):
    wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
    search_box = driver.find_element(By.XPATH, search_box_path)
    search_box.send_keys(Keys.CONTROL + 'a')
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(name)
    wait_component.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listitem']//span[@title='{name}']"))).click()


def search_unsave_contact(number: int) -> object:
    try:
        wait_component.until(EC.element_to_be_clickable((By.XPATH, new_chat_path))).click()
        wait_component.until(EC.presence_of_element_located((By.XPATH, search_box_unsave_chat_path)))
        search_box_new_chat = driver.find_element(By.XPATH, search_box_unsave_chat_path)
        search_box_new_chat.send_keys(Keys.CONTROL + 'a')
        search_box_new_chat.send_keys(Keys.DELETE)
        search_box_new_chat.send_keys(number)
        wait_component.until(EC.presence_of_element_located((By.XPATH, unsave_contact_path)))
        sleep(0.2)
        wait_component.until(EC.element_to_be_clickable((By.XPATH, unsave_contact_path))).click()
    except Exception as e:
        return {"response": f"Erro na procura do contato: {e}"}
        


def direct_message(name:str, message: str) -> object:
    try:
        search_contact(name)
        send_message(message)
        response = {"response": "Mensagem Enviada"}
    
    except Exception as e:
        response = {"error": f"A mensagem não foi enviada: {e}"}

    finally:
         return response

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


def send_image_for_save_contact(name: int, file: any):
    item = os.path.realpath(file)

    try:

        search_contact(name)
        wait_component.until(EC.element_to_be_clickable(
            (By.XPATH, attach_path))).click()
        wait_component.until(
            EC.presence_of_element_located((By.XPATH, file_path)))
        arquivo = driver.find_element(By.XPATH, file_path)
        arquivo.send_keys(item)
        wait_component.until(EC.element_to_be_clickable(
            (By.XPATH, send_button_path))).click()
        sleep(1)
        wait_component.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, wait_icon_path)))
        response = {"response"}

    except Exception as e:
        response = {"error": f"Não foi possivel enviar a imagem: {e}"}

    finally:
        return response


