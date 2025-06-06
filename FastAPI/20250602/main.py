from fastapi import FastAPI, Request, HTTPException
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
    
# CRUD 중 Create 기능
# {}안에 있는건 경로 매개변수
@app.post("/items/{item_id}", response_model=Item)
def create_item(item_id:int, item:Item):
    if item_id in items:
        # item_id가 items에 있다는것이 참이라면 문제가 있다(예외처리를 해야한다)
        # raise : 강제로 에러를 터뜨린다 / 강제로 예외를 발생시키다.
        # status_code : 실패니까 400
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

# CRUD 중 Read 기능
# List[Item] : Item만으로 이루어진 List를 반환
@app.get("/items", response_model=List[Item])
def read_items():
    return list(items.values())

# 키 값들만 반환하기
@app.get("/items-keys", response_model=List[int])
def read_keys():
    return list(items.keys())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id:int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
