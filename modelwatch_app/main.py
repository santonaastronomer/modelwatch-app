from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os

from mangum import Mangum

# from modelwatch_app.api.api_v1.api import router as api_router
from modelwatch_app.core.config import API_V1_STR, PROJECT_NAME
from routers import mlperformance
from routers import datalayout


app = FastAPI(
    title=PROJECT_NAME, # if not custom domain openapi_prefix="/prod"
)


# app.include_router(api_router, prefix=API_V1_STR)
app.include_router(mlperformance.router)
app.include_router(datalayout.router)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/ping")
# def pong():
#     """
#     Sanity check.

#     This will let the user know that the service is operational.

#     And this path operation will:
#     * show a lifesign

#     """
#     return {"ping": "pong!"}
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


handler = Mangum(app, enable_lifespan=False)


