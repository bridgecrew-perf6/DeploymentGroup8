from multiprocessing import Value

from django.db.models import Q, F
from django.forms import CharField
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def index(request):
    # Query all posts
    products = Product.objects.all()
    return render(request, 'shop/base.html', {'products': products})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')


    if query is not None:
        products = Product.objects.all()
        products = products.filter(description__icontains=query)
    return render(request, 'shop/product/list.html', {'products': products})
