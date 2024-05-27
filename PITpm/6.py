from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):

    #Обработчик запросов GET к эндпоинту "/items/{item_id}".

 
    #item_id: ID товара, получаемый из пути запроса. Должен быть целым числом от 0 до 1000.
    #q: Строковый параметр запроса (query parameter).
    #Числовой (float) параметр запроса. Должен быть больше 0 и меньше 10.5.

    #Словарь, содержащий ID товара и, при наличии, значение параметра q.
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
