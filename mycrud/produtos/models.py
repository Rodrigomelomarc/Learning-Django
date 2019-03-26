from django.db import models


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    categoria = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.TimeField(auto_now=True)
