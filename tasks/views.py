from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 
                  "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, 
                  "signup.html",
                  {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password= request.POST['password1']
                )
                user.save()
                login(request, user)
                return render(request, "tasks.html")
            
            except IntegrityError:
                return render(request,
                              "signup.html",
                              {'form': UserCreationForm,
                               'error': "El usuario ya existe"})

def tasks(request):
    return render(request, 
                  "tasks.html")

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == "GET":
        return render(request, 
                  "signin.html",
                  {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            return render(request,
                          "signin.html",
                          {'form': AuthenticationForm,
                           'error': "Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect('tasks')

    
    
  



