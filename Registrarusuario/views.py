from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout

# Create your views here.
def hello(request):
    return render(request, 'registrarusuario.html',{
        'form': UserCreationForm
    })
    
def registrarusuario(request):
    if request.method == 'GET':
        return render(request, 'registrarusuario.html',{
            'form': UserCreationForm
        }) 
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:                
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'registrarusuario.html',{
                'form': UserCreationForm,
                'error': 'Usuario ya existe'
                })
        return render(request, 'registrarusuario.html',{
                'form': UserCreationForm,
                'error': 'Contraseñas no coinciden'
                })        
        

def tasks(request):
    return render(request, 'task.html')

def salir(request):
    logout(request)
    return redirect('registrarusuario')