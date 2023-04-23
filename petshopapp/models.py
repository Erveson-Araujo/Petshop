from django.db import models
from uuid import uuid4


class Petshopapp(models.Model):
    id_petshop = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    nome_do_tutor = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50, default=uuid4)
# Create your models here.


class Cadastro(models.Model):
    id_petshop = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    nome_dono = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50, default=uuid4)
