from django.contrib import admin
from . models import Post

@admin.register(Post) # -> python의 장식자 문법
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    search_fields = ["title"]
    list_filter = ["status"]