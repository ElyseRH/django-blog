from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)  # trailing comma important, otherwise py will read as string instead of tuple
        