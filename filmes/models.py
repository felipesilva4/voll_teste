from django.db import models

# Create your models here.

class Filmes (models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()
    url=models.CharField(max_length=3000)