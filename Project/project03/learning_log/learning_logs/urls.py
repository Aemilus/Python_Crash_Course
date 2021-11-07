"""Defines URL patterns for Learning Logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page that shows all the topics
    path('topics/', views.topics, name='topics'),
    # page for a single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]
