from rest_framework import viewsets
from petshopapp.api import serializers
from petshopapp import models


class PetshopappViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PetshopappSerializer
    queryset = models.Petshopapp.objects.all()


class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadastroSerializer
    queryset = models.Cadastro.objects.all()
