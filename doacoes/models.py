from django.db import models
from estoque.models import Produto

class EntidadeParceira(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    entidade = models.ForeignKey(EntidadeParceira, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_doacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} para {self.entidade.nome}"