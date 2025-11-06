from django.db import models

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    idade = models.IntegerField()