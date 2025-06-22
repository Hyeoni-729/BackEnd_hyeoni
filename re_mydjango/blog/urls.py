from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_List),
    path("<int:pk>/", views.post_detail),
    path("<int:post_pk>/comments/new/", views.Comment_new),
]
