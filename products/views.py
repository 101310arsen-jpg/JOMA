from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

def catalog_view(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
        selected_category = category
    else:
        products = Product.objects.all()
        selected_category = None
    
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    
    return render(request, 'products/catalog.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']  
    search_fields = ['name', 'description'] 
    ordering_fields = ['price', 'name']  

def about_view(request):
    return render(request, 'products/about.html')

# Create your views here.
