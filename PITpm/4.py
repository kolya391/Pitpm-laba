from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# Определение Pydantic модели для объекта Item
class Item(BaseModel):
    name: str  # Название объекта, обязательное поле
    description: Union[str, None] = None  # Описание объекта, необязательное поле
    price: float  # Цена объекта, обязательное поле
    tax: Union[float, None] = None  # Налог на объект, необязательное поле


# Создание экземпляра FastAPI приложения
app = FastAPI()


# Определение PUT обработчика для маршрута "/items/{item_id}"
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    # Создание словаря результата, содержащего item_id и данные из объекта item
    result = {"item_id": item_id, *item.dict()}
    
    # Если параметр q передан в запросе, добавляем его в словарь результата
    if q:
        result.update({"q": q})
    
    # Возвращаем словарь результата в качестве ответа
    return result