from django.contrib import admin

from .models import Genero, Editora, Autor, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'genero')
    search_fields = ('titulo', 'editora__nome', 'genero')
    list_filter = ('editora', 'genero')
    ordering = ('titulo', 'editora', 'genero')
    list_per_page = 25