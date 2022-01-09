from .models import Message
from django import forms

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields=["id", "userId", "title", "body"]
        labels = {

            'id': 'Enter ID',
            'userId': 'Enter userID' ,
            'title': 'Enter title',
            'body': 'Enter body'
        }

        widgets = {

            'id': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ID' }),
            'userId': forms.TextInput(attrs={'class':'form-control','placeholder': 'userID'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'title'}),
             'body':forms.Textarea(attrs={'class':'form-control','placeholder':'body'})
        }