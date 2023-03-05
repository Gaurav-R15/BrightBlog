from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=300)  # String - title of blog post
    content = models.TextField()  # content of blog post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author of blog post
    pub_date = models.DateTimeField(auto_now_add=True)  # date and time that post was published
    category = models.CharField(max_length=300, default='Computer Science')

    def __str__(self):
        return self.title + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=[str(self.pk)])  # needed in order to enable uploading of posts directly from the site


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article')  # needed in order to enable uploading of posts directly from the site


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)  # post that is associated with
    # the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author of comment
    body = models.TextField()  # String - content of comment
    date = models.DateTimeField(auto_now_add=True)  # date and time that the comment was left
    upvotes = models.IntegerField(default=0)  # int - number of upvotes on the comment
    downvotes = models.IntegerField(default=0)  # int - number of downvotes on the comment

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s, commented on by %s' % (self.post.title, self.author)

