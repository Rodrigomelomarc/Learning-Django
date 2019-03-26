from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro-produtos/', views.cadastro_produtos,
         name='cadastro_produtos'),
    path('lista-produtos/', views.lista_produtos,
         name='lista_produtos'),
    path('adiciona-produto', views.adiciona_produtos,
         name='adiciona-adiciona_produtos'),
    path('remover/<int:id>', views.remover, name='remover'),
]
