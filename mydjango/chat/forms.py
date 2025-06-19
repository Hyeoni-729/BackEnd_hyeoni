from django import forms
from chat.models import PuzzleRoom

# 상속(Inheritance) 문법
class PuzzleRoomForm(forms.ModelForm):
    class Meta: # Meta는 정해져있다.
        model = PuzzleRoom
        # 지정 모델의 모든 모델 필드 내역을 읽고 자동 폼 필드 구성 해라
        fields = "__all__"

# 수정 시에는 레벨만 수정을 허용하고 싶다하면
class PuzzleRoomEditForm(forms.ModelForm):
    class Meta: # Meta는 정해져있다.
        model = PuzzleRoom
        fields = ["level"]