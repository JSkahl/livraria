from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Genero
from livraria.serializers import GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer