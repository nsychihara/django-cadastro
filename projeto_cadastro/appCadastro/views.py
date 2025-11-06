from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novoUsuario = Usuario()
    novoUsuario.nome = request.POST.get('nome')
    novoUsuario.idade = request.POST.get('idade')
    novoUsuario.save()
    