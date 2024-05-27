# импортируем FastAPI
from fastapi import FastAPI

# создаем экземпляр приложения FastAPI
app = FastAPI()

# создаем маршрут обработчика для GET запроса на /items/{item_id}
# принимаем параметры item_id (строка), needy (строка), skip (целое число, значение по умолчанию 0), limit (целое число или None)
# функция обработчик возвращает словарь с полученными параметрами
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item