from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import success

# Create your views here.

def create_account(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            success(request, 'Welcome User!')
            return redirect(to='')
    return render(request,'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            success(request, 'Logged in Successfully')
            login(request, user)
            redirect(to='deck_list')

        else:
            error(request, 'Invalid login')

    return render(request, '')


def logout(request):
    logout(request)
    redirect(to='')
