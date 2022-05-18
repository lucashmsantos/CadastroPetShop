from django.db import models
from uuid import uuid4

class Cadastro(models.Model):
    id_cachorro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    porte = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    idade = models.IntegerField()
    dono = models.CharField(max_length=255)