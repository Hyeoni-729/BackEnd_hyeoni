# config/urls.py 수정
from django.contrib import admin
from django.urls import path
from django.urls import include  # ADDED

urlpatterns = [
    path("admin/", admin.site.urls),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로 chat/ 이라는 prefix 주소를 부여하겠다.
    path("chat/", include("chat.urls")),  # ADDED
]
