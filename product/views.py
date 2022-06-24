from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from exention.throttling import CustomThrottlingUser
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, ProductType, ProductSpecification
from .serializers import (
    CategoryListSerializer,
    CategoryInputSerializers,
    ProductTypeSerializer,
    ProductTypeDetailSerializer,
    ProductTypeInputSerializer,
    ProductSpecificationListSerializer,
    ProductSpecialInputSerializers
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

    def get_throttles(self):
        """
        user can 4 post request per second, for create notice object
        CustomThrottlingUser ==> /throttling.py
        :return:
        """
        throttle_classes = (CustomThrottlingUser,)
        return [throttle() for throttle in throttle_classes]

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
        category = get_object_or_404(Category, slug=slug, is_active=True)

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


class ProductTypeViewSet(ViewSet):

    def get_permissions(self):
        """
        just superuser can create and update and destroy category
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = ()

        return [permission() for permission in permission_classes]

    def get_throttles(self):
        """
        user can 4 post request per second, for create notice object
        CustomThrottlingUser ==> /throttling.py
        :return:
        """
        throttle_classes = (CustomThrottlingUser,)
        return [throttle() for throttle in throttle_classes]

    def list(self, request):
        """
        show list product type object
        :param request:
        :return:
        """
        product_type_list = ProductType.objects.active()
        serializer = ProductTypeSerializer(instance=product_type_list, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        create product_type object
        :param name:char, is_active:bool
        """
        serializer = ProductTypeInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create product_type object successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        show product_type object
        :param slug:
        :return:
        """
        product_type = get_object_or_404(ProductType, pk=pk, is_active=True)

        serializer = ProductTypeDetailSerializer(instance=product_type, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """
        update product_type object by pk field
        you can change name:char , is_active:bool
        :return:
        """
        product_type = get_object_or_404(ProductType, pk=pk)
        serializer = ProductTypeInputSerializer(product_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        destroy product_type object by pk field
        :param pk:
        :return:
        """
        product_type = get_object_or_404(ProductType, pk=pk)
        product_type.delete()
        return Response({'status': 'deleted object'}, status=status.HTTP_200_OK)


class ProductSpecificationViewSet(ViewSet):
    def get_permissions(self):
        """
        just superuser can create and update and destroy object
        """
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = ()

        return [permission() for permission in permission_classes]

    def get_throttles(self):
        """
        user can 4 post request per second, for create notice object
        CustomThrottlingUser ==> /throttling.py
        :return:
        """
        throttle_classes = (CustomThrottlingUser,)
        return [throttle() for throttle in throttle_classes]

    def create(self, request):
        """
        create product_specification object
        :param name:char , product_type_name:char
        """
        serializer = ProductSpecialInputSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create product_special object successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
