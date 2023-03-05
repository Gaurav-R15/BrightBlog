
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('authentication/', include('django.contrib.auth.urls')),
    path('authentication/', include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
]