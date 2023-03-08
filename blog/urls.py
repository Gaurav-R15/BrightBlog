from django.urls import path  # allows us to designate URL paths in our website
# this next line allows us to import our Views so that we may associate them with our website's URLs
from .views import HomeView, ArticleView, NewPostView, EditPostView, DeletePostView, NewCommentView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # homepage URL
    path('post/<int:pk>', ArticleView.as_view(), name='article'),  # URL of a specific Post
    path('new_post/', NewPostView.as_view(), name="new_post"),  # URL of New Post form
    path('post/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),  # URL of Edit Post form
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),  # URL of Delete Post form
    path('post/<int:pk>/comment', NewCommentView.as_view(), name='new_comment'),  # URL of New Comment form
    path('like/<int:pk>', LikeView, name='like_comment'),  # URL that enables us to execute code in LikeView via POST
]
