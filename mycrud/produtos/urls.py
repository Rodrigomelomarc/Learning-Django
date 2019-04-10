from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-produtos/', views.lista_produtos,
         name='lista_produtos'),
    path('adiciona-produto', views.adiciona_produtos,
         name='adiciona_produtos'),
    path('remover/<int:id>', views.remover_produtos, name='remover'),
    path('atualiza/<int:id>', views.atualiza_produto,
         name='atualiza_produto'),
]
