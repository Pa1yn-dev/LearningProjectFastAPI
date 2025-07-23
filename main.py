from fastapi import FastAPI
from enum import Enum

class Helicopters(str, Enum):
    kiowa = "kiowa"
    apache = "apache"
    chinook = "chinook"

test_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
app = FastAPI()

#Path parameters:

@app.get("/")
async def root():
    return {"messsage" : "Hello World"}

@app.get("/retrieve/{id}")
async def read_item(id : int):
    return {"item_id" : id}

@app.get("/retrieve/helicopter/{heli_name}")
async def get_helicopter(heli_name : Helicopters):
    if heli_name is Helicopters.kiowa:
        return {"heli_name": heli_name, "message": "OH-58D"}
    if heli_name.value == "apache":
        return {"heli_name": heli_name, "message": "AH-64D"}
    else:
        return {"heli_name": heli_name, "message": "CH-47F"}

#:path basically accepts a filepath such as "/home/peter/test.txt" as one parameter rather than an API endpoint"
@app.get("/files/{file_path:path}")
async def read_file(file_path : str):
    return {"file_path" : file_path}

#Query parameters:

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return test_db[skip : skip + limit]
