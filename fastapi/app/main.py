"""
Main module, starts the http service.
"""
import uvicorn
from fastapi import FastAPI
from app.logic.calc import add
from app.model.item import Item


server = FastAPI()


@server.get("/")
async def root():
    """
    Root HTTP endpoint with generic information.
    :return:
    """
    return {"message": "Hello World"}


@server.post("/addition/")
async def addition_item(item: Item):
    """
    Add HTTP endpoint that takes two numbers as argument.
    :param item: parameters
    :return:  output of the addition
    """
    item.result = add(item.x, item.y)
    return item


if __name__ == '__main__':
    uvicorn.run("app.main:server", host="0.0.0.0", port=8000, reload=True)
