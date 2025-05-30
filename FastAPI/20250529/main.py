# fastapi라는 모듈에 FastAPI라는 클래스를 가져온다
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()

notices = ["공지사항1", "공지사항2", "공지사항3"]

templates = Jinja2Templates(directory="templates")

# http 메서드가 get이면 정보를 가져오는것

# @app.get("/") : EndPoint
@app.get("/") # 경로지정 : 사용자가 / 경로로 접근했을 때 아래 함수를 실행해라
def read_root(): # 경로에 대한 함수
  return {"Name": "luvi"}

# 이걸 실행시키고 싶을 때 쓰는 터미널 명령어
# uvicorn main:app --reload 여기서 main은 .py 앞 이름으로 쓰면 된다

@app.get("/good")
def read_goo():
  return {"a":1}

@app.get("/users")
def get_users():
  return {"a":1, "b":2}

@app.get("/todo")
def todo():
  return {"Name":"luvi", "Age":20}

@app.get("/undo")
def undo():
  return {"hello":2025}

@app.get("/info")
def info():
  return {
    "Name":"luvi",
    "adr":{
      "zipcode":12345,
      "adr1":"울산광역시",
      "adr2":"중구"
    }
  }

@app.post("/")
def post():
  return {"This":"is post"}

@app.get("/")
def read_root():
  return {"Hello":"World"}

@app.get("/about")
def about():
  return {"message":"about page"}

@app.get("/contact")
def contact():
  return {"message":"contact page"}

@app.get("/notice")
def get_notice():
  return notices

# 기본 응답 값은 json인데 response_class를 지정해주면 html로 응답
@app.get("/index", response_class=HTMLResponse)
def index():
  return '<h1>hello</h1>'

@app.get("/index2", response_class=HTMLResponse)
def index():
  return '''
  <h1>hello world</h1>
  <p>hello</p>
  <ol>
    <li>1</li>
    <li>2</li>
    <li>3</li>
  </ol>
'''

@app.get("/index3")
def index2(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})