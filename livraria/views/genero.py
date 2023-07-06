from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from livraria.models import Genero
from livraria.serializers.genero import GeneroSerializer

from rest_framework.permissions import IsAuthenticated


class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticated]