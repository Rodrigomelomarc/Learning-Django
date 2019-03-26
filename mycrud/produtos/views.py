from django.shortcuts import render, redirect
from .forms import ProdutosForm
from .models import Produtos
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def cadastro_produtos(request):
    return render(request, 'cadastro_produtos.html')


def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista-produtos.html', {'produtos': produtos})


def adiciona_produtos(request):
    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'cadastro_produtos.html')
