from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# django view : http 요청을 받아 요청을 처리하는 함수
# django에서는 클래스로 View를 만든다 -> 클래스 기반 뷰
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능

# 채팅 기본 화면을 보여줌
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html/")

# 매 채팅 메세지를 받아, 응답 메세지를 만들고, 응답한다.
# HTTP Methods : GET, POST, PUT/PATCH, DELETE, OPTIONS
# - HTTP : 웹 페이지, 웹 문서를 위한 프로토콜
# - 기본 <form method=""> 태그(유저로부터 입력을 받아 지정 서버로 전송)에서는 GET, POST만 지원
#   - GET : 조회 목적<요청해도 데이터는 변하지 않는다 => 검색엔진은 항상 GET요청>, POST : 추가/수정/삭제 등
#     - 조회목적인데 POST 요청을 하는 서비스가 있다(필요하면 하면 됨). 단,  가급적이면 조회에서는 GET 요청을 쓰고 서비스 최적화 여지가 많고 이를 도와주는 서비스/프로그램도 많다.
# - JS API를 통해서 PUT/PATCH, DELETE 등의 요청 가능 
def chat_message_new(request: HttpRequest) -> HttpResponse:
    # Query Parameters
    request.GET #QueryDict 타입 (Dict로 보여도 90% 무방), Post 요청에도 있을 수 있다
    request.POST  # POST 데이터(QueryDict)

    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문 없음"
    
    return HttpResponse(answer)