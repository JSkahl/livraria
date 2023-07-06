from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from livraria.models import Livro
from livraria.serializers.livro import LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return LivroDetailSerializer
        elif self.action == "retrieve":
            return LivroSerializer
        return LivroSerializer