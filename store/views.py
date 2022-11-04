from django.shortcuts import get_object_or_404, render
from .models import Product
from app.models import Category

def store(request, category_slug=None):
    if category_slug == None:
        store_product = Product.objects.filter(is_available=True)
    else:
        categorys = get_object_or_404(Category, slug=category_slug)
        store_product = Product.objects.filter(is_available=True, category=categorys)
    data = {
        'store_p':store_product,
        'count': store_product.count
    }
    return render(request, 'shop.html', data)

def detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
    context = {
        'product':product,
    }
    return render(request, 'detail.html', context)