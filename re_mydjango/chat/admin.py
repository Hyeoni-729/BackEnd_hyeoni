from django.contrib import admin
from .models import PuzzleRoom


@admin.register(PuzzleRoom)
class PuzzleRoomAdmin(admin.ModelAdmin):
    pass
