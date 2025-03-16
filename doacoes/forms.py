from django import forms
from django.utils import timezone  # Adicione esta linha
from .models import Doacao, EntidadeParceira
from estoque.models import Produto

class EntidadeParceiraForm(forms.ModelForm):
    class Meta:
        model = EntidadeParceira
        fields = ['nome', 'endereco', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['produto', 'entidade', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'entidade': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra produtos que estão próximos ao vencimento
        self.fields['produto'].queryset = Produto.objects.filter(validade__lte=timezone.now() + timezone.timedelta(days=7))