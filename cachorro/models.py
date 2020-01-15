from django.db import models
from dono.models import Dono

class Cachorro(models.Model): 

    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    porte = models.CharField(max_length=255)
    cor_do_pelo = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('PARDO', 'Pardo'),

    )

    cor = models.CharField(choices=cor_do_pelo, max_length=100)
    dono = models.ManyToManyField(Dono, null=True)

# Create your models here.
