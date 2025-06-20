from django.contrib import admin
from . models import Post

# admin.site.register(Post) -> 첫 번째 방법

# # 두 번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass

# # PostAdmin 룰에 맞춰 admin에 등록해라
# admin.site.register(Post, PostAdmin)

# 세 번째 방법
@admin.register(Post) # -> python의 장식자 문법
class PostAdmin(admin.ModelAdmin):
    pass