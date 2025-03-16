from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]