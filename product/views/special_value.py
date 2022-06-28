from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from exention.throttling import CustomThrottlingUser
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import ProductSpecification, ProductSpecificationValue
from product.serializers import (
    ProductTypeInputSerializer,
    ProductSpecificationListSerializer,
    ProductSpecialInputSerializers,
    ProductSpecialValueInputSerializers
)
from django.shortcuts import get_object_or_404


class ProductSpecificationValueViewSet(ViewSet):

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
        create product_specification_value object
        :param value:char , product_slug:char,product_special_name:char
        """
        serializer = ProductSpecialValueInputSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create product_special_value object successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        update product_special_value object by name field
        :param value:char , product_slug:char,product_special_name:char
        """
        product_special_value = get_object_or_404(ProductSpecificationValue, pk=pk)
        serializer = ProductSpecialValueInputSerializers(product_special_value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        destroy product_special_value object by pk field
        :param pk:int
        :return:
        """
        product_special_value = get_object_or_404(ProductSpecificationValue, pk=pk)
        product_special_value.delete()
        return Response({'status': 'deleted object'}, status=status.HTTP_200_OK)
