from django.shortcuts import render, redirect
from .forms import ProdutosForm
from .models import Produtos
from django.contrib import messages
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')


def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista-produtos.html', {'produtos': produtos})


def adiciona_produtos(request):

    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'cadastro_produtos.html', {'form': form})


def remover_produtos(request, id):
    produto = get_object_or_404(Produtos, pk=id)

    produto.delete()
    return redirect('lista_produtos')


def atualiza_produto(request, id):
    produto = Produtos.objects.get(id=id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if request.method == "POST":
        if form.is_valid:
            form.save()
            messages.success(request, 'Produto atualizado com sucesso')
            return redirect('lista_produtos')

    return render(request, 'atualiza-form.html', {'form': form,
                                                  'produto': produto})
