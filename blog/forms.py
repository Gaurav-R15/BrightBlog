from django import forms  # allows us to use Django's default forms module to craft our forms
from .models import Post, Comment  # import models so that we may use them to base our forms off of
from bootstrap_modal_forms.forms import BSModalModelForm  # import BSModalModelForm in order to design a pop-up form


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This is where we put together the basic components of our PostForm, which is used to add a new Post to the site.
It utilizes Django's default model form, ModelForm. We present the Post's title, image, category, and content as form
fields that the User can provide input for. We automatically set the author of the post to be the User who is logged in
and making the Post in our View for the form. We also automatically set the DateTime of the Post to be the date and time
at which the Post is created.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # form will be designed around the Post model, so we designate that model
        fields = ('title', 'image', 'content')  # indicate the fields to be displayed in order

        """""""""
        This bottom component breaks down our fields into individual elements in order to style them in 
        each field's most appropriate way.
        """""""""
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Here we put together the components for our PostEdit form, which allows us to edit a Post. Note that only the content
and title of the post are included as fields, since categories and images are more than likely to be final: it is 
incredibly hard to select the wrong category or image and we assume for now that the User will select the appropriate
values for these fields. This could be changed to include a Post's image and category in the future.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'content', 'title'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body of Post'}),
        }


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
This is the set-up for our pop-up Comment form. It makes use of the BSModalModelForm (Bootstrap Modal Model Form)
in order to be able to render our form inside a Bootstrap Modal with the support of some JS and Ajax, which is included
in the same template where our posts and comments are displayed (article_detail.html). The only field we include here
is the Comment body, as both the author and date are automatically set when the Comment is created.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class CommentForm(BSModalModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Drop your thoughts here...'}),
        }
