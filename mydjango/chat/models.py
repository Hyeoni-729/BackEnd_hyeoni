from django.db import models

# 게임방 필요한 거
# - 이름 / 이미지 파일 / level


# DB 생성(1개) + 테이블 생성 (N개)
## 엑셀로 따지면 : 워크북 생성(1개) + 워크시트 생성 (N개)


# ORM
class PuzzleRoom(models.Model):
    LEVEL_CHOICES = [
        (3, "Level 3"),
        (4, "Level 4"),
        (5, "Level 5"),
    ]

    # 이미지 확인 후, 특정 폴더에 저장하고 나서 저장 경로를 DB에 저장
    image_file = models.ImageField(upload_to="chat/puzzle/")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
