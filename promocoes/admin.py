from django.contrib import admin
from .models import RegraDesconto

@admin.register(RegraDesconto)
class RegraDescontoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'porcentagem_desconto', 'dias_antes_vencimento', 'ativo')
    list_filter = ('ativo', 'dias_antes_vencimento')
    search_fields = ('produto__nome',)  # Busca pelo nome do produto