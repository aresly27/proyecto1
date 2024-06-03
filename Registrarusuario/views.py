from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello(request):
    return render(request, 'registrarusuario.html',{
        'form': UserCreationForm
    })
    
def registrarusuario(request):
    return render(request, 'registrarusuario.html',{
        'form': UserCreationForm
    })