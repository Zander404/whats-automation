from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Annotated
import requests
import AllWhatsPy as awp
from time import sleep
from PIL import Image
from tempfile import NamedTemporaryFile
import io

app = FastAPI(title="Serverzinho")

awp.conexao(2)

@app.get("/sim")
def home():
    return {"Hello": "Word"}


@app.post("/teste/", tags=["teste", "zap"])
def teste(number: str, msg: str) -> None:
    try:
        awp.encontrar_usuario(number)
        awp.enviar_mensagem(msg)
    except:
        return{"error": "PAU NO SEU CU"}
        
    return {"data": "Mensagem enviada"}


@app.post("/zap/mensagem/", tags=["teste"])
async def enviar_mensage(number: str, msg:str):

    try:
        awp.encontrar_usuario(number)
    except:
        return HTTPException(status_code=400, detail="Erro de Envio")

@app.post("/zap/foto/", tags=["zap"])
async def enviar_imagem(number: str, image: UploadFile = File(...)):


    # with NamedTemporaryFile(suffix=".jpg") as temp_file:
    #     images.save(temp_file.name)
    #     print (f"save {temp_file.name} in /tmp")
    try:

        awp.encontrar_usuario(number)
        awp.enviar_imagem(image.file)
    except:
        return HTTPException(status_code=400, detail="Erro de Envio de Imagem") 
        
@app.post("/zap/video/", tags=["zap"])
async def enviar_video():
    try:
        awp.encontrar_contato()
        awp.enviar_mensagem("teste")
    except:
        return HTTPException(status_code=400, detail="Muito erro")
