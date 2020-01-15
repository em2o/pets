from django.db import models

# Create your models here.
from dono.models import Dono


class Gatinho(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cor_do_pelo = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('PARDO', 'Pardo'),
        ('cinza','cinza'),
        ('laranja','laranja'),
        ('bege','bege'),
        ('tricolor','tricolor'),
        ('laranja','laranja'),

    )
    cor = models.CharField(choices=cor_do_pelo, max_length=100)
    dono = models.ManyToManyField(Dono, null=True)