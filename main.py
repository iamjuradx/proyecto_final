from fastapi import FastAPI
from controller.location_controller import router as r1
from controller.typedoc_controller import router as r2
from controller.person_controller import router as r3

app = FastAPI(title="FastAPI DIVIPOLA Example")

app.include_router(r1)
app.include_router(r2)
app.include_router(r3)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}