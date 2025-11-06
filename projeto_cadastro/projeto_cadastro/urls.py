from django.urls import path
from appCadastro import views

urlpatterns = [
    path('',views.home,name='home'),
    path('usuario/',views.usuario,name='listagemUsuario'),
    path('deletarUsuario/<int:idUsuario>/', views.deletarUsuario, name='deletarUsuario'),
]
