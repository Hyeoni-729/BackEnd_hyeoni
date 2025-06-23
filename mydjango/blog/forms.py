from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # ModelForm을 쓰면 무조건 class 안에 class가 와야함
    class Meta:
        model = Comment
        # 전체 필드를 지정할 때는 [](리스트)를 쓰지 않음
        fields = ["content"]