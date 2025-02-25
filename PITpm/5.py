from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    
    Обработчик запросов GET к эндпоинту "/items/".
    #hidden_query: Необязательный строковый параметр запроса, который не будет включен в документацию Swagger.
    #Словарь, содержащий значение параметра hidden_query или сообщение "Not found", если параметр не передан.
    
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}