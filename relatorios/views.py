from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from io import BytesIO
from django.utils import timezone
from estoque.models import Produto
from doacoes.models import Doacao
from promocoes.models import RegraDesconto


def relatorio_desperdicio(request):
    produtos = Produto.objects.all()
    doacoes = Doacao.objects.all()
    promocoes_ativas = RegraDesconto.objects.filter(ativo=True)

    hoje = timezone.now().date()

    # Produtos doados (IDs)
    produtos_doados_ids = doacoes.values_list('produto_id', flat=True)

    # Produtos com promoção ativa (IDs)
    produtos_promocao_ids = promocoes_ativas.values_list('produto_id', flat=True)

    # Montar o relatório
    data = []
    for produto in produtos:
        status = 'Estoque'

        # Se o produto está vencido
        if produto.validade and produto.validade < hoje:
            # Se foi doado ou vendido com promoção ativa, não é desperdício
            if produto.id in produtos_doados_ids:
                status = 'Doado'
            elif produto.id in produtos_promocao_ids:
                status = 'Vendido com Desconto'
            else:
                status = 'Desperdício'

        data.append({
            'Produto': produto.nome,
            'Quantidade': produto.quantidade,
            'Status': status,
        })

    df = pd.DataFrame(data)

    # Gerar gráfico de status
    chart_data = df.groupby('Status').size().reset_index(name='Quantidade')

    context = {
        'chart_data': chart_data.to_dict('records'),
        'tabela': df.to_dict('records'),
    }
    return render(request, 'relatorios/relatorio_desperdicio.html', context)


def exportar_relatorio_csv(request):
    produtos = Produto.objects.all()
    doacoes = Doacao.objects.all()
    promocoes_ativas = RegraDesconto.objects.filter(ativo=True)

    hoje = timezone.now().date()

    produtos_doados_ids = doacoes.values_list('produto_id', flat=True)
    produtos_promocao_ids = promocoes_ativas.values_list('produto_id', flat=True)

    data = []
    for produto in produtos:
        status = 'Estoque'

        if produto.validade and produto.validade < hoje:
            if produto.id in produtos_doados_ids:
                status = 'Doado'
            elif produto.id in produtos_promocao_ids:
                status = 'Vendido com Desconto'
            else:
                status = 'Desperdício'

        data.append({
            'Produto': produto.nome,
            'Quantidade': produto.quantidade,
            'Validade': produto.validade,
            'Status': status,
        })

    df = pd.DataFrame(data)

    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.csv"'
    return response
