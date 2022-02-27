from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register(request):
    """Register new user."""
    if request.method != 'POST':
        # blank registration form
        form = UserCreationForm()
    else:
        # process filled registration form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # login new_user and redirect to homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
