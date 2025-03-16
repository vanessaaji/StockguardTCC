from django.shortcuts import render, get_object_or_404, redirect
from .models import RegraDesconto
from .forms import RegraDescontoForm

def lista_promocoes(request):
    promocoes = RegraDesconto.objects.filter(ativo=True)
    return render(request, 'promocoes/lista_promocoes.html', {'promocoes': promocoes})

def adicionar_promocao(request):
    if request.method == 'POST':
        form = RegraDescontoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_promocoes')
    else:
        form = RegraDescontoForm()
    return render(request, 'promocoes/adicionar_promocao.html', {'form': form})

def editar_promocao(request, id):
    promocao = get_object_or_404(RegraDesconto, id=id)
    if request.method == 'POST':
        form = RegraDescontoForm(request.POST, instance=promocao)
        if form.is_valid():
            form.save()
            return redirect('lista_promocoes')
    else:
        form = RegraDescontoForm(instance=promocao)
    return render(request, 'promocoes/editar_promocao.html', {'form': form})

def excluir_promocao(request, id):
    promocao = get_object_or_404(RegraDesconto, id=id)
    if request.method == 'POST':
        promocao.ativo = False  # Desativa a promoção em vez de excluir
        promocao.save()
        return redirect('lista_promocoes')
    return render(request, 'promocoes/excluir_promocao.html', {'promocao': promocao})