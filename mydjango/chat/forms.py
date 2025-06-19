from django import forms
from chat.models import PuzzleRoom

# 상속(Inheritance) 문법
class PuzzleRoomForm(forms.ModelForm):
    class Meta: # Meta는 정해져있다.
        model = PuzzleRoom
        fields = "__all__"