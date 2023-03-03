from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # form will be designed around the Post model, so we designate that model
        fields = ('title', 'author', 'pub_date', 'content')  # indicate the fields to be displayed in order

        """""""""
        This bottom component breaks down our fields into individual elements in order to style them in 
        each field's most appropriate way.
        """""""""
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'pub_date': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }


class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }
