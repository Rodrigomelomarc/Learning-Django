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


def remover_produtos(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    return redirect('lista_produtos')


def atualiza_produto(request, id):
    produto = Produtos.objects.get(id=id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if form.is_valid:
        form.save()
        messages.success(request, 'Produto atualizado com sucesso')
        return redirect('lista_produtos')

    return render(request, 'atualiza-form.html')


def atualiza_form(request, id):
    produto = Produtos.objects.get(id=id)
    return render(request, 'atualiza-form.html', {'produto': produto})
