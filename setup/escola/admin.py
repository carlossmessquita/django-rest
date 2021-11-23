from django.contrib import admin
from .models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 20


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)
    list_per_page = 5


# Register your models here.
admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
