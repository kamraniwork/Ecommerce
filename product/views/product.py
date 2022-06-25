from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from exention.throttling import CustomThrottlingUser
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import ProductSpecification, Product
from product.serializers import (
    ProductTypeInputSerializer,
    ProductSpecificationListSerializer,
    ProductSpecialInputSerializers,
    ProductListSerializer
)
from django.shortcuts import get_object_or_404


class ProductViewSet(ViewSet):
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
        show list product objects
        """
        product_list = Product.objects.filter(is_active=True)
        serializer = ProductListSerializer(instance=product_list, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
