from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'validade', 'quantidade', 'fornecedor')  # Campos exibidos na lista
    list_filter = ('categoria', 'validade')  # Filtros laterais
    search_fields = ('nome', 'fornecedor')  # Campos de busca