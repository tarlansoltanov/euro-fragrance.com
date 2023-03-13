from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from ..base.models import BaseSetting


def shop(request, template_name='products/shop.html', context={}):
    context['title'] = 'Shop'
    context['settings'] = BaseSetting.objects.first()
    context['categories'] = Category.objects.filter(main=None)

    page = request.GET.get('page', 1)
    products = Product.objects.all()
    paginator = Paginator(products, 11)

    context['page'] = paginator.get_page(page)
    context['page'].adjusted_elided_pages = paginator.get_elided_page_range(page)

    return render(request, template_name, context)

def product(request, pk, template_name='products/product.html', context={}):
    context['title'] = 'Product'
    context['settings'] = BaseSetting.objects.first()
    context['categories'] = Category.objects.filter(main=None)

    context['product'] = get_object_or_404(Product, pk=pk)
    # Related Products
    context['products'] = Product.objects.filter(categories__in=context['product'].categories.all()).exclude(pk=pk).distinct()

    return render(request, template_name, context)

def category(request, pk, template_name='products/shop.html', context={}):
    category = get_object_or_404(Category, pk=pk)

    context['title'] = category.name
    context['settings'] = BaseSetting.objects.first()
    context['categories'] = Category.objects.filter(main=None)

    page = request.GET.get('page', 1)
    products = Product.objects.filter(categories__in=category.subcategories.all()).distinct() if category.subcategories.exists() else Product.objects.filter(categories__in=[category])
    paginator = Paginator(products, 11)

    context['page'] = paginator.get_page(page)
    context['page'].adjusted_elided_pages = paginator.get_elided_page_range(page)

    return render(request, template_name, context)