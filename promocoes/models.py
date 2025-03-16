from django.db import models
from estoque.models import Produto

class RegraDesconto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    porcentagem_desconto = models.DecimalField(max_digits=5, decimal_places=2)
    dias_antes_vencimento = models.IntegerField()  # Dias antes do vencimento para aplicar o desconto
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.porcentagem_desconto}%"