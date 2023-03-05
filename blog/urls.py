from django.urls import path
#from . import views
from .views import HomeView, ArticleView, NewPostView, EditPostView, DeletePostView, NewCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', ArticleView.as_view(), name='article'),
    path('new_post/', NewPostView.as_view(), name="new_post"),
    path('post/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('new_category/', NewCategoryView.as_view(), name="new_category"),
    path('category/<str:categories>/', CategoryView, name='category'),
]