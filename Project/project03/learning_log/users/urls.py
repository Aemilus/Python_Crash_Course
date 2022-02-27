"""Define URL patterns for users."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # include default auth urls, such as login and logout
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]
