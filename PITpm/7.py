from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


# Определение Pydantic модели для объекта Item
class Item(BaseModel):
    name: str  # Название объекта, обязательное поле
    description: str | None = None  # Описание объекта, необязательное поле 
    price: float  # Цена объекта, обязательное поле
    tax: float | None = None  # Налог на объект, необязательное поле 


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,  # ID элемента, получаемый из URL пути
    item: Annotated[Item, Body(embed=True)],  # Объект Item, передаваемый в теле запроса 
):
    
    #Обработчик PUT-запросов к эндпоинту "/items/{item_id}" для обновления товара.

        #item_id: ID товара, получаемый из пути запроса.
        #item: Объект Item, содержащий данные для обновления товара. Передается в теле запроса и встраивается в него.

        #Словарь, содержащий ID товара и объект Item с обновленными данными.

    results = {"item_id": item_id, "item": item}
    return results