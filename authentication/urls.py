from django.urls import path
from .views import UserSignupView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='register'),
]