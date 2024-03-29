from django.shortcuts import render, get_object_or_404, get_list_or_404
from goods.models import Products, Categories
from django.core.paginator import Paginator


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, per_page=3)
    concurrent_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'goods': concurrent_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product_slug = Products.objects.get(slug=product_slug)

    context = {
        'product': product_slug,
    }

    return render(request, 'goods/product.html', context=context)
