from django import forms
from .models import Post, Category, Comment

categories = Category.objects.all().values_list('name', 'name')
category_list = []

for item in categories:
    category_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # form will be designed around the Post model, so we designate that model
        fields = ('title', 'author', 'category', 'content')  # indicate the fields to be displayed in order

        """""""""
        This bottom component breaks down our fields into individual elements in order to style them in 
        each field's most appropriate way.
        """""""""
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }


class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'content', 'title'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'body'}

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
