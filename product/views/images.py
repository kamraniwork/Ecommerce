from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from exention.throttling import CustomThrottlingUser
from rest_framework.response import Response
from product.models import ProductType, ProductImage
from product.serializers import (
    ProductTypeSerializer,
    ProductTypeDetailSerializer,
    ProductTypeInputSerializer,
    ProductImageListSerializer,
    ProductImageInputSerializer
)
from django.shortcuts import get_object_or_404


class ProductImageViewSet(ViewSet):

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
        show list product image object
        """
        product_image_list = ProductImage.objects.all()
        serializer = ProductImageListSerializer(instance=product_image_list, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        create product_image object
        """
        serializer = ProductImageInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'create product_image object successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        update product_image object by pk field
        :return:
        """
        product_image = get_object_or_404(ProductImage, pk=pk)
        serializer = ProductImageInputSerializer(product_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("update object", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        destroy product_image object by pk field
        :param pk
        """
        product_image = get_object_or_404(ProductImage, pk=pk)
        product_image.delete()
        return Response({'status': 'deleted object'}, status=status.HTTP_200_OK)
