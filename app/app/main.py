from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request


app = FastAPI()


templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def get_root(request: Request):
    title = "Demo of FastAPI, Docker and K8s"
    message = "Hello World!"
    return templates.TemplateResponse("index.html", {"request": request, "title": title, "message": message})