from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer



def catalog_view(request, category=None):
    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.all()
    categories = Product.objects.values_list('category__name', flat=True).distinct()
    return render(request, 'products/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
    })


def cart_view(request):
    cart = request.session.get('cart', [])
    cart_items = []
    total = 0
    for item_id in cart:
        try:
            product = Product.objects.get(id=item_id)
            cart_items.append({'product': product, 'quantity': 1})
            total += float(product.price)
        except Product.DoesNotExist:
            pass
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart
    messages.success(request, "Товар добавлен в корзину!")
    return redirect('catalog')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    messages.info(request, "Товар удалён из корзины")
    return redirect('cart')


def contact_view(request):
    return render(request, 'products/contact.html')


def about_view(request):
    return render(request, 'products/about.html')



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'colors', 'sizes']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']
    ordering = ['price']


@api_view(['GET'])
def brand_info(request):
    return Response({
        "name": "JOMA",
        "founded": 1965,
        "country": "Испания",
        "mission": "Создание спортивной одежды высочайшего качества",
        "website": "https://www.joma-sport.com"
    })