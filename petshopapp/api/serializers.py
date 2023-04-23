from rest_framework import serializers
from petshopapp import models


class PetshopappSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Petshopapp
        fields = '__all__'


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadastro
        fields = '__all__'
