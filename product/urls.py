from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductTypeViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product-type', ProductTypeViewSet, basename='product-type')

# The API URLs are now determined automatically by the router.
app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
]
