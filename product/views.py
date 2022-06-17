from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category
from .serializers import (
    CategoryListSerializer,
    CategoryInputSerializers
)
from django.shortcuts import get_object_or_404


class CategoryViewSet(ViewSet):
    lookup_field = 'slug'

    def get_permissions(self):
        """
        just superuser can create and update and destroy category
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = ()

        return [permission() for permission in permission_classes]

    def list(self, request):
        """
        show list category object
        show all nested category (sub category)
        :param request:
        :return:
        """
        category_list = Category.objects.active()
        serializer = CategoryListSerializer(instance=category_list, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        create category object
        :param name:char, slug:char, parent_name:char
        if there is not parent_name ==> error 404
        parent_name can be None
        """
        serializer = CategoryInputSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create category object successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, slug=None):
        """
        show category object
        :param slug:
        :return:
        """
        category = get_object_or_404(Category, slug=slug)

        serializer = CategoryListSerializer(instance=category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, slug=None):
        """
        update object category by slug field
        you can change name:char , slug:char , parent_name:char(can null)
        :return:
        """
        category = get_object_or_404(Category, slug=slug)
        serializer = CategoryInputSerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        """
        destroy category object by slug field
        :param slug:
        :return:
        """
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response({'status': 'deleted object'}, status=status.HTTP_200_OK)
