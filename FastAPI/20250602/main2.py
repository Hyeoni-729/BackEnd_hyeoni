from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 간단한 데이터 저장소
messages = []

# html에서 문법(if, for)를 쓸 땐 {%...%}, 변수를 쓸 땐{{...}}

# home.html을 볼 수 있는 화면 구동
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """메인 페이지 - 데이터를 템플릿에 전달"""
    context = {
        "request": request,  # jinja2templates 쓸라면 필수!
        "title": "안녕하세요!",
        "message_count": len(messages),
        "messages": messages,
    }
    return templates.TemplateResponse("home.html", context)

# form.html을 볼 수 있는 화면 구동
@app.get("/write", response_class=HTMLResponse)
def write_form(request: Request):
    """글쓰기 폼 페이지"""
    context = {
        "request": request,
        "title": "메시지 작성"
    }
    return templates.TemplateResponse("form.html", context)

# result.html을 볼 수 있는 화면 구동
## 동적 웹페이지
@app.post("/write", response_class=HTMLResponse)
def write_message(request: Request, name: str = Form(...), message: str = Form(...)):
    """폼 데이터 받아서 처리"""
    # 새 메시지 저장
    new_message = {"name": name, "message": message}
    messages.append(new_message)
    
    # 결과 페이지 보여주기
    context = {
        "request": request,
        "title": "작성 완료",
        "name": name,
        "message": message
    }
    return templates.TemplateResponse("result.html", context)