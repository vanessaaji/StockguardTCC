from django.contrib import admin
from .models import EntidadeParceira, Doacao

@admin.register(EntidadeParceira)
class EntidadeParceiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')
    search_fields = ('nome', 'endereco')

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'entidade', 'quantidade', 'data_doacao')
    list_filter = ('data_doacao', 'entidade')
    search_fields = ('produto__nome', 'entidade__nome')
