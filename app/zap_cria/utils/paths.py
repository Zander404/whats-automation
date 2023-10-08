

"""
Paths para Inicio

"""
init_path = '//*[@id="app"]/div/div/div[4]/header'

"""
TEXT PATH'S
"""

search_box_path: str = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]' # Caixa de Pesquisa de Contatos/Grupos
message_box_path: str = '//div[@role="textbox"][@title="Digite uma mensagem"]' # Caixa de Mensagem

new_chat_path: str = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
search_box_unsave_chat_path = '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]'
unsave_contact_path = '//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[2]' 



"""
FILE PATH'S
"""
attach_path: str = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'
image_video_path: str = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div'
file_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input'
send_button_path = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'


"""
ICON'S PATH'S
"""

wait_icon_path = 'span[data-icon="msg-time"]'