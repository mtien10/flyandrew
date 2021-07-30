from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=request.POST['password1'])
            auth_login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login(request):
    return render(request, 'registration/login.html')
# Create your views here ok.
