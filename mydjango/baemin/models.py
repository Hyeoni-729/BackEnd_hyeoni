from django.db import models

# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField # FileField : 모든 파일 포맷 저장 가능
    photo = models.ImageField() # ImageField : 이미지만 받는다

# N측 : 1에 대한 외래키 필드 추가
class Review(models.Model):
    # 가게에 대한 리뷰들은 자동으로 shop이 삭제될때 같이 삭제된다
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField() # 별점입력(적은 단위 숫자)