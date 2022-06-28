from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from exention.throttling import CustomThrottlingUser
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import ProductSpecification
from product.serializers import (
    ProductTypeInputSerializer,
    ProductSpecificationListSerializer,
    ProductSpecialInputSerializers,
    ProductSpecialListInputSerializer
)
from django.shortcuts import get_object_or_404


class ProductSpecificationViewSet(ViewSet):
    lookup_field = 'name'

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

    def list(self, request):
        """
        show list product_special objects
        """
        product_special = ProductSpecification.objects.all()
        serializer = ProductSpecialListInputSerializer(instance=product_special, context={'request': request},
                                                       many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def update(self, request, name=None):
        """
        update product_special object by name field
        you can change name:char , product_type_name:char
        """
        product_special = get_object_or_404(ProductSpecification, name=name)
        serializer = ProductTypeInputSerializer(product_special, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, name=None):
        """
        destroy product_special object by name field
        :param name:char
        :return:
        """
        product_special = get_object_or_404(ProductSpecification, name=name)
        product_special.delete()
        return Response({'status': 'deleted object'}, status=status.HTTP_200_OK)
