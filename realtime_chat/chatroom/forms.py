from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['title']


class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))