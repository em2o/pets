from django.db import models

# Create your models here
class Dono(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome