from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_list),
    path("<int:pk>/", views.shop_detail),
    path("<int:shop_pk>/reviews/new/", views.review_new),
]
