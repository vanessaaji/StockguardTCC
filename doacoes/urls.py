from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_doacoes, name='lista_doacoes'),
    path('adicionar/', views.adicionar_doacao, name='adicionar_doacao'),
    path('entidades/', views.lista_entidades, name='lista_entidades'),
    path('entidades/adicionar/', views.adicionar_entidade, name='adicionar_entidade'),
]