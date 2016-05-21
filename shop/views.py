import string
from decimal import Context
from macpath import join

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.utils.crypto import random

from shop.models import Product, Category
from shop.my_functions import categories_generate, products_generate


def home(request):
    products = Product.objects.all()
    if request.GET:
        product_name = request.GET['product_name']
        products = products.filter(name__contains=product_name)
    categories = Category.objects.all()
    context = {
            'categories': categories,
            'products': products
    }
    if request.POST:
        categories_generate()
        products_generate()
        return HttpResponse('Товары были сгенерированы')
    return render(request, 'shop/home.html', context)
def show_product(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    categories = Category.objects.all()

    form = {}
    errors = []
    if request.POST:
        form['name'] = request.POST.get('name')
        form['category'] = Category.objects.get(id=request.POST.get('category_id'))
        form['price'] = request.POST.get('price')
        form['description'] = request.POST.get('description')

        if not form['name']:
            errors.append('Введите название товара')
        if not form['price']:
            errors.append('Укажите цену')
        if not form['description']:
            errors.append('Введите описание товара')
        if not errors:
            product.name = form['name']
            product.category = form['category']
            product.price = form['price']
            product.description = form['description']
            product.save()
            return HttpResponse('Карточка была изменена')

    context = {
        'product': product,
        'categories': categories,
        'errors': errors,
        'form' : form
    }

    return render(request,'shop/product.html',context)
def category(request,category_id):
    category = get_object_or_404(Category, id = category_id)
    categories = Category.objects.all()
    products = Product.objects.all().filter(category=category)
    if request.GET:
        product_name = request.GET['product_name']
        products = products.all().filter(name__contains=product_name)
    context = {
        'categories' : categories,
        'products' : products
    }
    return render(request, 'shop/category.html', context)

