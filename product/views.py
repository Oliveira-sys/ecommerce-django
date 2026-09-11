from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


from .models import Product


def productList(request):
    query = Product.objects.all()

    contexto = {
        'query': query
    }

    return render(request, 'products/product_page.html', contexto)


def productListView(request, id = None):
    query = get_object_or_404(Product, id=id)
    contexto = {
        'query': query
    }

    return render(request, 'products/details.html', contexto)
