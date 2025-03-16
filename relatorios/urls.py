from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorio_desperdicio, name='relatorio_desperdicio'),
    path('exportar_csv/', views.exportar_relatorio_csv, name='exportar_relatorio_csv'),
]