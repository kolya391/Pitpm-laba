# Импортирование класса FastAPI из библиотеки FastAPI
from fastapi import FastAPI

# Создание экземпляра класса FastAPI
app = FastAPI()

# Определение маршрута HTTP GET "/items/{item_id}", где {item_id} является динамическим параметром
# Функция read_item принимает item_id в качестве параметра и возвращает словарь с ключом "item_id" и значением item_id
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}