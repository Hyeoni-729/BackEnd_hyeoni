from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField # FileField : 모든 파일 포맷 저장 가능
    photo = models.ImageField() # ImageField : 이미지만 받는다

# 장고의 유효성 검사 함수 : 항상 1개의 인자만 받는다.
# 그 값이 정해진 규칙에서 벗어날 때, ValidationError 예외 발생
# 정해진 규칙에 부합이 될 때, Nothing to do : 그냥 함수 종료. 반환값 필요 없음

# def validator_min_1(value):
#     """인자의 값이 1 이상이기를 기대"""
#     if value < 1:
#         raise ValidationError("값이 1이상이 되어야 합니다.")
    
# 위 def문(함수)를 만들어주는 함수를 구현해보자.
def make_validator_min(min_value):
    min_value = 1
    def validator_func(value):
        if value < min_value:
            raise ValidationError(f"값이 {min_value}이상이 되어야 합니다.")
    return validator_func

# validator_min_1 = make_validator_min(1)

# N측 : 1에 대한 외래키 필드 추가
class Review(models.Model):
    # 가게에 대한 리뷰들은 자동으로 shop이 삭제될때 같이 삭제된다
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        # validators=[
        #     MinValueValidator(1), # 가급적 장고 기본에서 지원하는 Validators를 최대한 활용
        #     # make_validator_min(1), # 함수가 함수를 생성한 버전
        #     MaxValueValidator(5)], # 클래스를 함수처럼 사용한 버전
        choices=[
            (1, '1점'),
            (2, '2점'),
            (3, '3점'),
            (4, '4점'),
            (5, '5점'),
        ],
        help_text="점수를 고르세요"
    ) # 별점입력(적은 단위 숫자)