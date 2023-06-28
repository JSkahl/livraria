from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Genero, Editora, Autor, Livro
from livraria.serializers import GeneroSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return LivroDetailSerializer
        elif self.action == "retrieve":
            return LivroSerializer
        return LivroSerializer