from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('category/<str:category>/', views.catalog_view, name='catalog_category'),
    path('about/', views.about_view, name='about'),
]