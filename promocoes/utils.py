from datetime import timedelta
from django.utils import timezone
from estoque.models import Produto
from promocoes.models import RegraDesconto
from doacoes.models import Doacao, EntidadeParceira

def gerenciar_promocoes_doacoes():
    hoje = timezone.now().date()
    produtos = Produto.objects.filter(validade__gte=hoje)
    entidade_padrao = EntidadeParceira.objects.first()  
    for produto in produtos:
        dias_para_vencer = (produto.validade - hoje).days
        
        # Perecíveis (frutas, verduras, laticínios)
        if produto.categoria.lower() in ['frutas', 'verduras', 'legumes', 'laticínios']:
            if dias_para_vencer <= 2:
                Doacao.objects.create(
                    produto=produto,
                    entidade=entidade_padrao,
                    quantidade=produto.quantidade
                )
                produto.quantidade = 0
                produto.save()
            elif dias_para_vencer <= 5:
                RegraDesconto.objects.update_or_create(
                    produto=produto,
                    defaults={
                        'porcentagem_desconto': 50,
                        'dias_antes_vencimento': dias_para_vencer,
                        'ativo': True
                    }
                )
        
        # Não-perecíveis
        else:
            if dias_para_vencer <= 7:
                desconto = 40 if dias_para_vencer <= 3 else 25
                RegraDesconto.objects.update_or_create(
                    produto=produto,
                    defaults={
                        'porcentagem_desconto': desconto,
                        'dias_antes_vencimento': dias_para_vencer,
                        'ativo': True
                    }
                )