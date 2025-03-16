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
    promocoes = RegraDesconto.objects.filter(ativo=True)

    # Converter timezone.now() para date
    hoje = timezone.now().date()

    # Criar DataFrame com Pandas
    data = {
        'Produto': [p.nome for p in produtos],
        'Quantidade': [p.quantidade for p in produtos],
        'Status': [
            'Desperdício' if p.validade and p.validade < hoje else 'Estoque'
            for p in produtos
        ],
    }
    df = pd.DataFrame(data)

    # Gerar gráfico
    chart_data = df.groupby('Status').size().reset_index(name='Quantidade')

    context = {
        'chart_data': chart_data.to_dict('records'),
    }
    return render(request, 'relatorios/relatorio_desperdicio.html', context)

def exportar_relatorio_csv(request):
    produtos = Produto.objects.all()
    data = {
        'Produto': [p.nome for p in produtos],
        'Quantidade': [p.quantidade for p in produtos],
        'Validade': [p.validade for p in produtos],
    }
    df = pd.DataFrame(data)

    # Exportar para CSV
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    # Criar a resposta HTTP com o arquivo CSV
    response = HttpResponse(buffer, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.csv"'
    return response


'''
código de trabalho futuro para melhorar a exebição de relatório :
def relatorio_desperdicio(request):
    produtos = Produto.objects.all()
    doacoes = Doacao.objects.all()
    promocoes = RegraDesconto.objects.filter(ativo=True)

    hoje = timezone.now().date()

    data = {
        'Produto': [p.nome for p in produtos],
        'Quantidade': [p.quantidade for p in produtos],
        'Status': [
            'Desperdício' if p.validade and p.validade < hoje and not (
                Doacao.objects.filter(produto=p).exists() or
                RegraDesconto.objects.filter(produto=p, ativo=True).exists()
            ) else 'Estoque'
            for p in produtos
        ],
    }
    df = pd.DataFrame(data)

    chart_data = df.groupby('Status').size().reset_index(name='Quantidade')

    context = {
        'chart_data': chart_data.to_dict('records'),
    }
    return render(request, 'relatorios/relatorio_desperdicio.html', context)

'''