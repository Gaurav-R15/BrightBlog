from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, PostEdit, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class HomeView(generic.ListView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'home.html'  # utilizes the template we have created for this View
    ordering = ['-pub_date']


class ArticleView(generic.DetailView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'article_detail.html'  # utilizes the template we have created for this View


class NewPostView(generic.CreateView):
    model = Post  # sets the designated model to be used as Post
    form_class = PostForm  # implements bootstrapping that we designed for our "create a new blog post" form
    template_name = 'new_post.html'  # utilizes the template we have created for this View
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewCommentView(BSModalCreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(generic.UpdateView):
    model = Post  # sets the designated model to be used as Post
    form_class = PostEdit  # implements bootstrapping that we designed for our "edit a new blog post" form
    template_name = 'edit_post.html'  # utilizes the template we have created for this View


class DeletePostView(generic.DeleteView):
    model = Post  # sets the designated model to be used as Post
    template_name = 'delete_post.html'  # utilizes the template we have created for this View
    success_url = reverse_lazy('home')



