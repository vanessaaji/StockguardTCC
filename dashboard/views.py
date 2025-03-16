from django.shortcuts import render
from estoque.models import Produto
from doacoes.models import Doacao
from django.utils import timezone

def dashboard_view(request):
    # Data atual
    hoje = timezone.now().date()

    # Produtos vencidos (validade < hoje)
    produtos_vencidos = Produto.objects.filter(validade__lt=hoje)

    # Produtos próximos ao vencimento (hoje <= validade <= hoje + 7 dias)
    produtos_proximos_vencimento = Produto.objects.filter(
        validade__gte=hoje,
        validade__lte=hoje + timezone.timedelta(days=7)
    )

    # Totais
    total_estoque = Produto.objects.count()
    total_doacoes = Doacao.objects.count()

    context = {
        'produtos_vencidos': produtos_vencidos,
        'produtos_proximos_vencimento': produtos_proximos_vencimento,
        'total_estoque': total_estoque,
        'total_doacoes': total_doacoes,
    }
    return render(request, 'dashboard/dashboard.html', context)