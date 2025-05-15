from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controller.location_controller import router as r1
from controller.typedoc_controller import router as r2
from controller.person_controller import router as r3

app = FastAPI()

# incluye tus routers de API
app.include_router(r1)
app.include_router(r2)
app.include_router(r3)

# templates = Jinja2Templates(directory="templates")
# @app.get("/", response_class=HTMLResponse)
# async def serve_html(request: Request):
#  return templates.TemplateResponse("index.html", {"request": request})
@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}", tags=["root"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}