from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.http import Http404
from chat.models import PuzzleRoom
from chat.forms import PuzzleRoomForm

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
    request.GET  # QueryDict 타입 (Dict로 보여도 90% 무방), Post 요청에도 있을 수 있다
    request.POST  # POST 데이터(QueryDict)

    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문 없음"

    return HttpResponse(answer)


def puzzle_room(request, name):
    try:
        image_url = {
            "mario": "/static/chat/mario.jpg",
            "toy": "/static/chat/toy-story.jpg",
            "openai-1": "/static/chat/openai-1.png",
        }[name]
    except KeyError:
        # 위에서 from django.http import Http404
        raise Http404(f"not found room : {name}")

    level = 4

    return render(
        request,
        template_name="chat/puzzle.html",
        context={"image_url": image_url, "level": level},
    )


def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs},
    )


def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    # qs = PuzzleRoom.objects.all()

    # id 값을 통해, 아래 값을 찾아서 할당

    room = PuzzleRoom.objects.get(id=id)
    image_url = room.image_file.url
    level = room.level

    return render(
        request,
        template_name="chat/puzzle.html",
        context={
            "image_url": image_url,
            "level": level,
        },
    )


# 1개의 PuzzleRoom 생성을 위해서, 최소 2번의 요청을 받을거다.
def puzzleroom_new(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        # 1) GET 요청 : 빈 입력 서식을 보여줘야 함
        form = PuzzleRoomForm()
    else:
        form = PuzzleRoomForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/chat/puzzle/")
        else:
            pass

    return render(
        request,
        "chat/puzzleroom_form.html",
        {
            "form": form,
        },
    )

    # 2) POST 요청 : 유저가 서식에 값을 채우고, 전송 혹은 저장 버튼을 눌렀을 때 유저의 입력값 전송(반복 될 수 있음)


def puzzleroom_edit(request: HttpRequest, id: int) -> HttpResponse:
    # DB에서 수정 대상 조회
    room = PuzzleRoom.objects.get(id=id)

    if request.method == "GET":
        form = PuzzleRoomForm(instance=room)
    else:
        form = PuzzleRoomForm(instance=room, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/chat/puzzle/")
        else:
            pass

    return render(
        request,
        "chat/puzzleroom_form.html",
        {
            "form": form,
        },
    )