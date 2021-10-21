from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/mlperformance", response_class=HTMLResponse)
async def mlperformance_home(request: Request):

    return templates.TemplateResponse("mlperformance.html", {"request": request})