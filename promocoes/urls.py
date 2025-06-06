from django.urls import path
from . import views
from .views import atualizar_promocoes 

urlpatterns = [
    path('', views.lista_promocoes, name='lista_promocoes'),
    path('adicionar/', views.adicionar_promocao, name='adicionar_promocao'),
    path('editar/<int:id>/', views.editar_promocao, name='editar_promocao'),
    path('excluir/<int:id>/', views.excluir_promocao, name='excluir_promocao'),
     path('atualizar/', atualizar_promocoes, name='atualizar_promocoes'),
]