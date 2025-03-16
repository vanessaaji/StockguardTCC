## autenticacao/urls.py
#
#from django.urls import path
#from . import views
#
#urlpatterns = [
#    path('', views.login_view, name='login'),  # Mude de '/login/' para '' para que o login seja a página principal
#    path('logout/', views.logout_view, name='logout'),
#    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
#]
#
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Rota para a tela de login
    path('logout/', views.logout_view, name='logout'),  # Rota para logout
    path('criar-conta/', views.criar_conta, name='criar_conta'),  # Rota para criar conta
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url='/login/'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/login/'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]