from django.db import models

from livraria.models import Autor, Genero, Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(decimal_places=0, default=0, max_digits=5, null=True, blank=True)

    genero = models.ForeignKey(
        Genero, on_delete=models.PROTECT, related_name="livros"
    )

    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

    autores = models.ManyToManyField(
        Autor, related_name="livros"
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"