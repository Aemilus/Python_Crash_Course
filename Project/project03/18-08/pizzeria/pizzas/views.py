from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    # home page for pizzas app
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Display all pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    """Display toppings for a pizza identified by id."""
    pizza = Pizza.objects.get(id=pizza_id)
    # the default related_name is the 'name_of_your_model' + '_set' => 'topping_set'
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
