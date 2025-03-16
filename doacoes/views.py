from django.shortcuts import render, redirect
from .models import Doacao, EntidadeParceira
from .forms import DoacaoForm, EntidadeParceiraForm

def lista_doacoes(request):
    doacoes = Doacao.objects.all()
    return render(request, 'doacoes/lista_doacoes.html', {'doacoes': doacoes})

def adicionar_doacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_doacoes')
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/adicionar_doacao.html', {'form': form})

def lista_entidades(request):
    entidades = EntidadeParceira.objects.all()
    return render(request, 'doacoes/lista_entidades.html', {'entidades': entidades})

def adicionar_entidade(request):
    if request.method == 'POST':
        form = EntidadeParceiraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entidades')
    else:
        form = EntidadeParceiraForm()
    return render(request, 'doacoes/adicionar_entidade.html', {'form': form})