from django import forms

class FiltroRelatorioForm(forms.Form):
    data_inicio = forms.DateField(label='Data Início', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    data_fim = forms.DateField(label='Data Fim', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))