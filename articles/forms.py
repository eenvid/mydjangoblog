from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.articles
        fields = ['title', 'slug', 'body', 'image']