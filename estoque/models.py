from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    validade = models.DateField()
    quantidade = models.IntegerField()
    fornecedor = models.CharField(max_length=100)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nome
