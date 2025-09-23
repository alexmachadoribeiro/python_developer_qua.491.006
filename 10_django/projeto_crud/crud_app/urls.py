from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_pessoa, name='cadastro_pessoa'),
    path('alterar/<int:id_pessoa>/', views.alterar_pessoa, name='alterar_pessoa'),
    path('deletar/<int:id_pessoa>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('buscar/', views.buscar_pessoa, name='buscar_pessoa'),
]