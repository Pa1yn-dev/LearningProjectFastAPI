from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messsage" : "Hello World"}

@app.get("/retrieve/{id}")
async def read_item(id : int):
    return {"item_id" : id}
