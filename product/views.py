from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import Http404


from .models import Product


def productList(request):
    query = Product.objects.all()

    contexto = {
        'query': query
    }

    return render(request, 'products/product_page.html', contexto)


def productListView(request, id = None):
    #query = get_object_or_404(Product, id=id)
    qs = Product.objects.filter(id=id)
    if qs.count() == 1:
        query = qs.first()
    else:
        raise Http404("Esse produto não existe!")

    contexto = {
        'query': query
    }

    return render(request, 'products/details.html', contexto)
