"""Define URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # add a new blog post
    path('new_post/', views.new_post, name='new_post'),
    # edit blog post page
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
