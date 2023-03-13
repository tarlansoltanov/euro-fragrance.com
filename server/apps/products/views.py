from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from ..base.models import BaseSetting


def shop(request, template_name='products/shop.html', context={}):
    context['title'] = 'Shop'
    context['settings'] = BaseSetting.objects.first()

    page = request.GET.get('page', 1)
    products = Product.objects.all()
    paginator = Paginator(products, 11)

    context['page'] = paginator.get_page(page)
    context['page'].adjusted_elided_pages = paginator.get_elided_page_range(page)

    return render(request, template_name, context)

def product(request, pk, template_name='products/product.html', context={}):
    context['title'] = 'Product'
    context['settings'] = BaseSetting.objects.first()

    context['product'] = get_object_or_404(Product, pk=pk)

    return render(request, template_name, context)