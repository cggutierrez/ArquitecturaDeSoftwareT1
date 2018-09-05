from django import forms
from .models import Comment


class Form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text'
        ]
        labels = {
            'text' : "Send new message"
        } 
