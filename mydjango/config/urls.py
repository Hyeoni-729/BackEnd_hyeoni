from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로 chat/ 라는 prefix 주소를 부여하겠다.
    path("chat/", include("chat.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
