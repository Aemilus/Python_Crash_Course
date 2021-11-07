from django.shortcuts import render

# Create your views here.


def index(request):
    # home page for pizzas app
    return render(request, 'pizzas/index.html')
