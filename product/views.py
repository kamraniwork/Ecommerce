from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category
from .serializers import (
    CategoryListSerializer
)
from django.shortcuts import get_object_or_404


class CategoryViewSet(ViewSet):
    lookup_field = 'slug'

    def list(self, request):
        category_list = Category.objects.active()
        serializer = CategoryListSerializer(instance=category_list, context={'request': request}, many=True)
        return Response(serializer.data)