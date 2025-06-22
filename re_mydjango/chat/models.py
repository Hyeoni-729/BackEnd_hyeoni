from django.db import models


class PuzzleRoom(models.Model):
    LEVEL_CHOICES = [
        (3, "Level 3"),
        (4, "Level 4"),
        (5, "Level 5"),
    ]
    image_file = models.ImageField(upload_to="chat/puzzle/")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
