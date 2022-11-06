from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates


app = FastAPI(docs_url=None, title="pyodide_ifcjs")

app.mount('/static' , StaticFiles(directory='static'), name='static')
TEMPLATES = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    context = {"request": request}
    return TEMPLATES.TemplateResponse("pyodide_ifcjs.html", context)

