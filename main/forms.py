from django.forms import ModelForm, TextInput, Textarea

from .models import *


def image(attrs):
    pass

class JuiceForm(ModelForm):
    class Meta:
        model = Juice
        fields = ['title','image','description','price']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'название статьи'
            }),
            "image": image(attrs={
                'class': "form-control",
                'placeholder': ' image'
            }),
            "description": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'текст статьи'
            }),
            "price": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'price'
            }),
            # "time_create": DateField,
            # "time_update": DateField,
            # "is_published": BooleanField()
        }

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title','image','details','price']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'название статьи'
            }),
            "image": image(attrs={
                'class': "form-control",
                'placeholder': ' image'
            }),
            "details": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'текст статьи'
            }),
            "price": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'price'
            }),
        }
