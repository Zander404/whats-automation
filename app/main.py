from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Annotated
import requests
import AllWhatsPy as awp
from time import sleep
from PIL import Image
from tempfile import NamedTemporaryFile
import io
import app.zap_cria.main as zap

app = FastAPI(title="Serverzinho")



@app.get("/sim")
def home():
    return {"Hello": "Word"}


@app.post("/teste/", tags=["teste", "zap"])
def teste(number: str, msg: str) -> None:
    try:
        zap.mensagem_direta(number,msg)    
    except:
        return{"error": "PAU NO SEU CU"}
        
    return {"data": "Mensagem enviada"}


@app.post("/zap/mensagem/", tags=["teste"])
async def enviar_mensage(name: str, msg:str):

    # try:
        zap.direct_message(name=name, message=msg)
    # except:
    #     return HTTPException(status_code=400, detail="Erro de Envio")

@app.post("/zap/foto/", tags=["zap"])
async def enviar_imagem(number: str, image: UploadFile = File(...)):
    # try:
    zap.send_image_for_save_contact(number, image)

    # except:
    #     return HTTPException(status_code=400, detail="Erro de Envio de Imagem") 
        
@app.post("/zap/video/", tags=["zap"])
async def enviar_video():
    try:
        awp.encontrar_contato()
        awp.enviar_mensagem("teste")
    except:
        return HTTPException(status_code=400, detail="Muito erro")
