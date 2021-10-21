from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/datalayout", response_class=HTMLResponse)
async def datalayout_home(request: Request):

    return templates.TemplateResponse("datalayout.html", {"request": request})