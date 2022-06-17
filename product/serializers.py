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


class CategoryInputSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    slug = serializers.SlugField(max_length=256)
    parent_name = serializers.CharField(max_length=256)

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')
        parent_name = validated_data.get('parent_name', None)

        parent = get_object_or_404(Category, is_active=True, name=parent_name)
        category = Category.objects.create(name=name, slug=slug, parent=parent)

        return category

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')
        parent_name = validated_data.get('parent_name', None)

        category = get_object_or_404(Category, slug=slug, name=parent_name)
        instance.name = name
        instance.slug = slug
        instance.parent = category

        instance.save()
        return instance
