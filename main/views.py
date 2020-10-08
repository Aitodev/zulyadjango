from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'main/index.html')


def shop(request):
    produ = Product.objects.all()
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'produ': produ,
        'products': products,
    }
    return render(request, 'main/shop.html', context)


def product(request, slug_product):
    product = get_object_or_404(Product, slug_product__iexact=slug_product)
    context = {
        'product': product,
    }
    return render(request, 'main/product-details.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'main/product-details.html', {'product': product})


