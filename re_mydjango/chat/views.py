from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.http import Http404
from chat.models import PuzzleRoom
from chat.forms import PuzzleRoomForm, PuzzleRoomEditForm

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html/")

def chat_message_new(request: HttpRequest) -> HttpResponse:
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
        raise Http404(f"not found room : {name}")

    level = 4

    return render(
        request,
        template_name="chat/puzzle.html",
        context={"image_url": image_url, "level": level},
    )


def puzzleroom_list(request):
    qs = PuzzleRoom.objects.all()
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs},
    )


def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:
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


def puzzleroom_new(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
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

def puzzleroom_edit(request: HttpRequest, id: int) -> HttpResponse:
    room = PuzzleRoom.objects.get(id=id)

    if request.method == "GET":
        form = PuzzleRoomEditForm(instance=room)
    else:
        form = PuzzleRoomEditForm(instance=room, data=request.POST, files=request.FILES)
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