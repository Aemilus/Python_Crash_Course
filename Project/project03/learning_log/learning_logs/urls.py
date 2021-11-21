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
    # page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding a new entry for a specific topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
