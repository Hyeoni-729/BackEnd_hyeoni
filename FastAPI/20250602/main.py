from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

items = {}


class Item(BaseModel):
    name: str
    description: Optional[str] = (
        None  # 이 설명에는 빈 값이 들어갈 수도 있다 / 반드시 필요가 없다
    )
    price: float
    # item의 기본값이 True
    active: bool = True


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# CRUD 중 Create 기능
## {}안에 있는건 경로 매개변수
@app.post("/items/{item_id}", response_model=Item)
def create_item(item_id: int, item: Item):
    if item_id in items:
        # item_id가 items에 있다는것이 참이라면 문제가 있다(예외처리를 해야한다)
        # raise : 강제로 에러를 터뜨린다 / 강제로 예외를 발생시키다.
        # status_code : 실패니까 400
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item


# CRUD 중 Read 기능
## List[Item] : Item만으로 이루어진 List를 반환
@app.get("/items", response_model=List[Item])
def read_items():
    return list(items.values())


## 키 값들만 반환하기
@app.get("/items-keys", response_model=List[int])
def read_keys():
    return list(items.keys())


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# CRUD 중 Update 기능
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    # 키 값을 통해 Item 타입의 value를 가져온다
    stored_item: Item = items[item_id]
    # 변경 전 출력
    print(
        f"stored_item name={stored_item.name} price={stored_item.price} description={stored_item.description}"
    )
    # update_data = item.dict 에 dict가 밑줄이 쳐지는 이유는 이제 쓰지 않는다. modeol_dump로 대신해서 써라.
    # class ItemUpdate에서 None필드를 제외한 입력된 것들만 dict타입으로 만들겠다.
    update_data = item.model_dump(exclude_unset=True)

    print(update_data)

    updated_item = stored_item.model_copy(update=update_data)

    # 변경 후 출력
    print(
        f"update_item name={updated_item.name} price={updated_item.price} description={updated_item.description}"
    )

    items[item_id] = updated_item
    return updated_item


# CRUD 중 Delete 기능
## 보통 삭제된 데이터는 반환 하지 않아서 response_model이 필요없다.
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    if item_id in items:
        raise HTTPException(status_code=404, detail="Item not found")
    # 완전히 제거 (hard delete)
    items.pop(item_id)
    # 복원 가능한 제거 (soft delete)로 바꿀려면


'''실습
1. put
2. items/{item_id}?active={True or False}
3. 활성화된 아이템은 다시활성화하지 못한다. (예외처리)
4. 반환되는 모델은 Item'''
@app.put("/items/{item_id}/active")
# 쿼리스트링 문법을 쓰면 status:bool=True(status:bool도 가능 단, status_code 값 필수)기본값을 줘야한다
def update_activate(item_id:int, status:bool):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    # items 안에는 아무 타입의 값이 다 들어가기 때문에 타입 추론을 위해 item:Item(타입 힌팅)을 써줘야 한다
    stored_item:Item = items[item_id]
    if stored_item.active == status:
        # 요청이 잘못 된것이니까 status_code는 400
        raise HTTPException(status_code=400, detail="이미 활성화되었거나 비활성화된 아이템입니다.")
    stored_item.active = status
    return stored_item