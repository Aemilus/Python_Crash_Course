"""Defines URL patterns for meal_plans."""

from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    # home page
    path('', views.index, name='index')
]
