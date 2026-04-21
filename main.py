from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import time
import psutil
import os

app = FastAPI()

modelo = load_model('modelo_petr4.keras')
scaler = MinMaxScaler()

class DadosEntrada(BaseModel):
    precos: list[float]

@app.get("/")
def inicio():
    return {"mensagem": "API de previsão PETR4 funcionando!"}

@app.get("/monitoramento")
def monitoramento():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    return {
        "cpu_percent": cpu,
        "memoria_total_mb": round(memoria.total / 1024 / 1024, 2),
        "memoria_usada_mb": round(memoria.used / 1024 / 1024, 2),
        "memoria_percent": memoria.percent
    }

@app.post("/prever")
def prever(dados: DadosEntrada):
    if len(dados.precos) != 60:
        return {"erro": "Envie exatamente 60 preços históricos"}
    
    inicio_tempo = time.time()
    
    precos = np.array(dados.precos).reshape(-1, 1)
    precos_normalizados = scaler.fit_transform(precos)
    entrada = precos_normalizados.reshape(1, 60, 1)
    
    previsao_normalizada = modelo.predict(entrada)
    previsao = scaler.inverse_transform(previsao_normalizada)
    
    tempo_resposta = round(time.time() - inicio_tempo, 4)
    
    return {
        "previsao_fechamento": round(float(previsao[0][0]), 2),
        "tempo_resposta_segundos": tempo_resposta
    }