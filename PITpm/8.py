from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# Определение Pydantic модели для объекта Item
class Item(BaseModel):
    name: str  # Название объекта, обязательное поле (строка)
    description: str | None = Field(
        default=None,  # Описание объекта, необязательное поле (строка или None)
        title="The description of the item",  # Заголовок для документации
        max_length=300,  # Максимальная длина описания - 300 символов
    )
    price: float = Field(
        gt=0,  # Цена объекта, обязательное поле (число с плавающей точкой, больше 0)
        description="The price must be greater than zero",  # Описание для документации
    )
    tax: float | None = None  # Налог на объект, необязательное поле (число с плавающей точкой или None)


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,  # ID элемента, получаемый из URL пути
    item: Item = Body(embed=True),  # Объект Item, передаваемый в теле запроса
):
    #Обработчик PUT-запросов к эндпоинту "/items/{item_id}" для обновления товара.

        #item_id: ID товара, получаемый из пути запроса.
        #item: Объект Item, содержащий данные для обновления товара. Передается в теле запроса и встраивается в него.


        #Словарь, содержащий ID товара и объект Item с обновленными данными.
    results = {"item_id": item_id, "item": item}
    return results