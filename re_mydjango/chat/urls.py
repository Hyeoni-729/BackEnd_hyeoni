from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("messages/new/", views.chat_message_new),
    path("puzzle/", views.puzzleroom_list),
    path("puzzle/<int:id>/", views.puzzleroom_play),
    path("puzzle/new/", views.puzzleroom_new),
    path("puzzle/<int:id>/edit", views.puzzleroom_edit),
]
