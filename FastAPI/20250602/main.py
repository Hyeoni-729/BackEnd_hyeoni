from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

items = {}

class Item(BaseModel):
    name: str
    description: Optional[str] = None  # 이 설명에는 빈 값이 들어갈 수도 있다 / 반드시 필요가 없다
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    