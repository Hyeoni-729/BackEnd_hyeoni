from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    name: str
    price: float = 0.0

@app.get("/item")
def item_list():
    return {"item": items}

@app.post("/item/create")
def create_item(item: Item):
    items.append(item)
    print(item.name, item.price)
    return {"item": item}

@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}

'''
실습1
1. 사용자 정보를 저장하는 POST 엔드포인트를 만들어보세요. 사용자 정보는 이름, 이메일, 나이를 포함해야 합니다. Pydantic 모델을 사용하여 데이터를 검증하세요. -> 사용자정보리스트에 추가(people)

2. 사용자정보 리스트(people [list]) -> 조회하기
email:str -> EmailStr 사용하려면 pip install email-validator 필요
'''
people = []
class User(BaseModel):
  name:str
  age:int
  email:str

@app.post("/users")
def create_user(user:User):
    people.append(user)
    return {"사용자 등록":user}

@app.get("/users")
def get_user():
    return {"사용자 목록":people}

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    del people[user_id - 1] # 인덱스 값에 위치한 값만 삭제
    #(4번째꺼 삭제하고 싶으면 인덱스는 3이지만 원래 위치 4를 넣는다)