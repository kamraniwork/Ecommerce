from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import category, product_special, product_type,product

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'category', category.CategoryViewSet, basename='category')
router.register(r'product-type', product_type.ProductTypeViewSet, basename='product-type')
router.register(r'product-specification', product_special.ProductSpecificationViewSet, basename='product-specification')
router.register(r'product', product.ProductViewSet, basename='product')

# The API URLs are now determined automatically by the router.
app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
]
