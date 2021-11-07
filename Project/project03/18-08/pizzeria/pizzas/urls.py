"""Defines URL patterns for pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # display all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # display toppings for a specific pizza
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]
