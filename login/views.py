from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout

# Create your views here.

def ingresar (request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        }) 
        
    else:
        user = authenticate(request, username=request.POST['username'], 
                password=request.POST['password1'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            #return redirect('')
            
        
    return render(request, 'signin.html',{
        'form': AuthenticationForm
    })

