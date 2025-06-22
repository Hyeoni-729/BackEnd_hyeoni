from django import forms
from chat.models import PuzzleRoom


class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = "__all__"


class PuzzleRoomEditForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = ["level"]
