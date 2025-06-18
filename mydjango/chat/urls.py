# chat/urls.py 파일 생성
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("messages/new/", views.chat_message_new),
    # path("puzzle/toy/", views.puzzle_room),
    # puzzle/ 주소 에 문자열 패턴이 있고, 뒤에 / 가 있으면
    path("puzzle/<str:name>/", views.puzzle_room),
]
