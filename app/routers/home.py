from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
async def index(request: Request):
	return templates.TemplateResponse("home/index.html", {"request":request})