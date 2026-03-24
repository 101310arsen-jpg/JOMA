from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Тестовая футболка",
            description="Описание тестового товара",
            price=1500,
            category="Футболки",
            image_url="https://example.com/test.jpg"
        )
    
    def test_product_creation(self):
        product = Product.objects.get(name="Тестовая футболка")
        self.assertEqual(product.price, 1500)
        self.assertEqual(product.category, "Футболки")
    
    def test_product_str(self):
        product = Product.objects.get(name="Тестовая футболка")
        self.assertEqual(str(product), "Тестовая футболка")

# Create your tests here.
