# crypto_ledger/main.py
from fastapi import FastAPI, HTTPException, status
from typing import List, Optional
import uvicorn
# Импортируем наши модули (пока будут пустыми, но мы их заполним)
import models
import crud # Будет использоваться позже
import dotenv
import os

dotenv.load_dotenv()
DEV = os.environ.get("DEV")

app = FastAPI(title="CryptoLedger API")

#  Главный маршрут
@app.get("/", summary="Приветствие API", response_description="Сообщение с приветствием")
def read_root():
    return {"message": "Добро пожаловать в CryptoLedger API!"}

@app.post("/transactions", summary="Создание транзакции", response_description="Детали созданной транзакции")
def create_transaction(transaction: models.TransactionCreate):
    ans = crud.create_transaction(transaction)
    ans.update({"message":"Транзакция успешно создана!"})
    return ans

@app.get("/transactions",summary="Получение всех транзакций",response_description="Список всех транзакций")
def get_transactions():
    ans = crud.get_transactions()
    ans.update({"message":"Блок успешно создан"})
    return ans

@app.post("/blocks/",summary="Создание блока",response_description="Детали блока")
def blocks():
    pass

if __name__ == "__main__":
    if not DEV:
        uvicorn.run(app, host="0.0.0.0", port = 8000)
