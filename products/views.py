from django.shortcuts import render
from .models import Product

def catalog_view(request, category=None):
    # Получаем все товары
    if category:
        products = Product.objects.filter(category=category)
        selected_category = category
    else:
        products = Product.objects.all()
        selected_category = None
    
    # Получаем уникальные категории
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    
    return render(request, 'products/catalog.html', context)

# Create your views here.
