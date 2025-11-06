from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

def usuario(request):
    if request.method == 'POST':
        novoUsuario = Usuario()
        novoUsuario.nome = request.POST.get('nome')
        novoUsuario.idade = request.POST.get('idade')
        novoUsuario.save()
        return redirect('listagemUsuario')

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def deletarUsuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, idUsuario=idUsuario)
    usuario.delete()
    return redirect('listagemUsuario')
