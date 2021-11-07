"""Defines URL patterns for pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
]
