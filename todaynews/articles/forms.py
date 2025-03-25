from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'date', 'author', 'resource', 'content']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "resource": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Источник'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }