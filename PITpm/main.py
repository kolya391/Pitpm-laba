# Импортируем класс FastAPI из модуля fastapi
from fastapi import FastAPI

# Создаем экземпляр класса FastAPI
app = FastAPI()

# Определяем маршрут для GET запроса к корневому URL "/"
@app.get("/")
async def root():
    # Возвращаем словарь с сообщением "Hello World"
    return {"message": "Hello World"}