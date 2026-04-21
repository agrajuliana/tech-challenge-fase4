# Tech Challenge Fase 4 — Previsão de Ações PETR4 com LSTM

## Contexto
Projeto desenvolvido para o Tech Challenge da Fase 4 da Pós Tech em Machine Learning Engineering — FIAP.

## Descrição
Modelo preditivo de deep learning utilizando redes neurais LSTM para prever o preço de fechamento da ação PETR4 (Petrobras) na bolsa de valores brasileira, com base em dados históricos de janeiro de 2018 a dezembro de 2024.

## Por que LSTM?
RNNs tradicionais sofrem do problema do vanishing gradient, os gradientes diminuem tanto durante o treinamento que a rede para de aprender dependências de longo prazo. O LSTM resolve isso com mecanismos de portas (gates) que controlam o que deve ser lembrado ou esquecido. O modelo é treinado via Backpropagation Through Time (BPTT), técnica específica para redes recorrentes que desenrola a rede no tempo para calcular os gradientes.

## Resultados do Modelo
- MAE: R$ 1.21
- RMSE: R$ 1.32
- MAPE: 4.14%

## Estrutura do Projeto
- `tech_challenge_fase4.ipynb` — notebook com coleta, pré-processamento, treino e avaliação do modelo
- `main.py` — API FastAPI para servir o modelo
- `Dockerfile` — container para deploy da API
- `requirements.txt` — dependências do projeto

## Pré-requisitos
- Python 3.11+
- Docker Desktop (para rodar com container)

## Como usar

### 1. Treinar o modelo
Abra o notebook `tech_challenge_fase4.ipynb` no Google Colab e execute todas as células. O modelo será salvo como `modelo_petr4.keras`.

### 2. Rodar a API localmente
pip install -r requirements.txt
uvicorn main:app --reload

### 3. Rodar com Docker
docker build -t api-petr4 .
docker run -p 8000:8000 api-petr4

## Endpoints

### GET /
Verifica se a API está funcionando.

### GET /monitoramento
Retorna métricas de CPU e memória em tempo real.

### POST /prever
Recebe 60 preços históricos e retorna a previsão do próximo dia.

Exemplo de requisição:
{"precos": [22.5, 22.8, 23.1, 23.0, 22.7, 23.2, 23.5, 23.8, 24.0, 23.9, 24.2, 24.5, 24.3, 24.8, 25.0, 25.2, 25.5, 25.3, 25.8, 26.0, 26.2, 26.5, 26.3, 26.8, 27.0, 27.2, 27.5, 27.3, 27.8, 28.0, 28.2, 28.5, 28.3, 28.8, 29.0, 29.2, 29.5, 29.3, 29.8, 30.0, 30.2, 30.5, 30.3, 30.8, 31.0, 31.2, 31.5, 31.3, 31.8, 32.0, 32.2, 32.5, 32.3, 32.8, 33.0, 33.2, 33.5, 33.3, 33.8, 34.0]}

Exemplo de resposta:
{"previsao_fechamento": 33.21, "tempo_resposta_segundos": 0.0312}

## Tecnologias
Python, TensorFlow, Keras, FastAPI, Docker, yfinance, scikit-learn, psutil

## Autores
Pós Tech Machine Learning Engineering — FIAP