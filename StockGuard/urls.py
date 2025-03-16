"""
URL configuration for StockGuard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Importe RedirectView para redirecionar

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração do Django
    path('login/', include('autenticacao.urls')),  # URLs do app de autenticação
    path('dashboard/', include('dashboard.urls')),  # URLs do app de dashboard
    path('estoque/', include('estoque.urls')),  # URLs do app de estoque
    path('promocoes/', include('promocoes.urls')),  # URLs do app de promoções
    path('doacoes/', include('doacoes.urls')),  # URLs do app de doações
    path('relatorios/', include('relatorios.urls')),  # URLs do app de relatórios

    # Redireciona a raiz ('/') para a tela de login ou dashboard
    path('', RedirectView.as_view(url='/login/')),  # Redireciona para a tela de login
    # Ou, se preferir redirecionar para o dashboard:
    # path('', RedirectView.as_view(url='/dashboard/')),
]