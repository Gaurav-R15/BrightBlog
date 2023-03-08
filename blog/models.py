from django.db import models  # import Django's model module so that we may seamlessly create models
from django.contrib.auth.models import User  # import Django's User model which we utilize in our application
from django.urls import reverse  # helps with redirects
from ckeditor.fields import RichTextField
from datetime import datetime, date

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
We define our Post model here. It consists of the attributes:
- title (CharField): title of post, CharField because it will be a fairly short String
- content (TextField): body of post, TextField to allow for longer blog posts
- author (ForeignKey): author of post, ForeignKey to map each Post to a User
- pub_date (DateTimeField): date and time that the post was published
    *NOTE*: (auto_now_add=True) enables immediate setting of our pub_date attr according to our current timezone
- category (CharField): category of post , CharField because it will be a short String
- image (ImageField): image associated with the post

The functions include:
- __str__(self): helps us return a String representation of the Post, this is mainly only used on the admin page
- get_absolute_url(self): description of this function is provided in a supplementary comment next to the function.
In short assists in allowing a User to visit the specific pages of a Post
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Post(models.Model):
    title = models.CharField(max_length=300)  # String - title of blog post
    content = RichTextField(blank=True, null=True)  # content of blog post
    # content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author of blog post
    pub_date = models.DateTimeField(auto_now_add=True)  # date and time that post was published
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article',
                       args=[str(self.pk)])  # needed in order to enable uploading of posts directly from the site


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
We define our Comment model here. It consists of the attributes:
- post (ForeignKey): the Post that the Comment is associated with, ForeignKey to establish a one-to-many relationship
- author (ForeignKey): the author of the comment, ForeignKey to map each Comment to a User, similar to our Post model
- body (TextField): body of comment, TextField to allow for longer comments, capped at 500 characters
- date (DateTimeField): date and time that the comment was posted
    *NOTE*: (auto_now_add=True) enables immediate setting of our date attr according to our current timezone
- likes (ManyToManyField): essentially a list of Users who have liked the specific comment, ManyToManyField due to the
fact that multiple users can like multiple comments on any given Post

The functions include:
- Meta: enables us to dictate the order in which Comment instances are pulled from the database. This is advantageous
because iterating through our comments in order to display them will result in the comments with the latest post dates
being pulled and displayed first
- __str__: helps us return a String representation of the Post, this is mainly only used on the admin page
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)  # post that is associated with
    # the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author of comment
    body = models.TextField(max_length=500)  # String - content of comment
    date = models.DateTimeField(auto_now_add=True)  # date and time that the comment was left
    likes = models.ManyToManyField(User, related_name="comment_likes")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s, commented on by %s' % (self.post.title, self.author)
