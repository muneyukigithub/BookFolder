from django import forms
from .models import Book
from django.contrib.auth.forms import AuthenticationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title","text","image")

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   