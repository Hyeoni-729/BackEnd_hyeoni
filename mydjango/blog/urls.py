from django.urls import path
from . import views

# 장고의 urls.py한테 장고가 요구하는 것은 단 하나.
# urlpatterns 이름의 리스트 => 이름에 오타가 있으면 절대 안 된다.
urlpatterns = [
    path("", views.post_List),
    path("<int:pk>/", views.post_detail),
    path("<int:post_pk>/comments/new/", views.comment_new),
]
