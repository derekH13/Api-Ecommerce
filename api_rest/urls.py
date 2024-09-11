
from django.contrib import admin
from django.urls import path, include

from . import views

# faz a ligação da url á uma função view
urlpatterns = [
    path('usuario/', views.get_user, name='get_all_users'),
    path('produto/', views.get_produto, name='get_all_produtos'),
    path('compra/', views.get_compra, name='get_all_compras'),

    # busca por categoria produtos
    path('produto/categoria/<str:categoria>', views.get_categoria),

    # busca por genero usuario
    path('usuario/genero/<str:gnr>', views.get_genero),

    # crud usuario
    path('usuario/data/', views.crud_usuario),

    # crud produto
    path('produto/data/', views.crud_produto),

    # crud compra
    path('compra/data/', views.crud_compra),
]
