from django import forms
from .models import RegraDesconto

class RegraDescontoForm(forms.ModelForm):
    class Meta:
        model = RegraDesconto
        fields = ['produto', 'porcentagem_desconto', 'dias_antes_vencimento', 'ativo']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'porcentagem_desconto': forms.NumberInput(attrs={'class': 'form-control'}),
            'dias_antes_vencimento': forms.NumberInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }