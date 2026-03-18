from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'get_sales_count']
    list_filter = ['category']
    search_fields = ['name', 'description']
    
    def get_sales_count(self, obj):

        return f"{obj.id * 10} продаж" 
    get_sales_count.short_description = 'Продажи'

admin.site.register(Product, ProductAdmin)

# Register your models here.
