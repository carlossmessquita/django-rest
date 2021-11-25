from django.db import models


# Create your models here.
class Aluno(models.Model):
    objects = models.Manager()
    nome = models.CharField(max_length=100, blank=True)
    rg = models.CharField(max_length=9, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    objects = models.Manager()
    niveis = (
        ('A', 'Avançado'),
        ('I', 'Intermediário'),
        ('B', 'Básico')
    )

    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(choices=niveis, max_length=1,
                             blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    objects = models.Manager()
    periodo = (
        ('M', 'Matutino'),
        ('N', 'Noturno'),
        ('I', 'Integral')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=periodo, blank=False, null=False, default='I')

