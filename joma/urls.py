from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('api/', include(router.urls)), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)