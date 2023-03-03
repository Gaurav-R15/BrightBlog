from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=300)  # String - title of blog post
    content = models.TextField()  # content of blog post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author of blog post
    pub_date = models.DateTimeField('Date Posted')  # date that post was published on

    def __str__(self):
        return self.title + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))  # needed in order to enable uploading of posts directly from the site



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # post that is associated with the comment
    comment_author = models.CharField(max_length=700)  # author of comment
    comment_body = models.CharField(max_length=500)  # String - content of comment
    comment_date = models.DateTimeField('Date Commented')  # date that the comment was left
    upvotes = models.IntegerField(default=0)  # int - number of upvotes on the comment
    downvotes = models.IntegerField(default=0) # int - number of downvotes on the comment

    def __str__(self):
        return self.comment_body


