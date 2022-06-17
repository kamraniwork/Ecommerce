from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)
from .models import (
    Category
)

User = get_user_model()


class CategoryListSerializer(serializers.ModelSerializer):
    """
    show list category
    support many nested category
    """

    def to_representation(self, obj):
        # Add any self-referencing fields here (if not already done)
        if 'branches' not in self.fields:
            self.fields['children'] = CategoryListSerializer(obj, many=True)
        return super(CategoryListSerializer, self).to_representation(obj)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent')
