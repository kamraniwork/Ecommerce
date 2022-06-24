from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from exention.throttling import CustomThrottlingUser
from rest_framework.response import Response
from product.models import ProductType
from product.serializers import (
    ProductTypeSerializer,
    ProductTypeDetailSerializer,
    ProductTypeInputSerializer
)
from django.shortcuts import get_object_or_404


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
