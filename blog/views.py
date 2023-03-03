from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm, PostEdit
from django.urls import reverse_lazy


class HomeView(generic.ListView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'home.html'  # utilizes the template we have created for this View


class ArticleView(generic.DetailView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'article_detail.html'  # utilizes the template we have created for this View


class NewPostView(generic.CreateView):
    model = Post  # sets the designated model to be used as Post
    form_class = PostForm  # implements bootstrapping that we designed for our "create a new blog post" form
    template_name = 'new_post.html'  # utilizes the template we have created for this View


class EditPostView(generic.UpdateView):
    model = Post  # sets the designated model to be used as Post
    form_class = PostEdit  # implements bootstrapping that we designed for our "edit a new blog post" form
    template_name = 'new_post.html'  # utilizes the template we have created for this View

class DeletePostView(generic.DeleteView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'delete_post.html'  # utilizes the template we have created for this View
    success_url = reverse_lazy('home')
