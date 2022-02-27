"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # reuse django default auth urls with base template
    path('', include('django.contrib.auth.urls')),
    # register page
    path('register/', views.register, name='register'),
]
