from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'release_date', 'price', 'image']
