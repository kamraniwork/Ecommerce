from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)
from .models import (
    Category,
    ProductType,
    ProductSpecification,
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
    parent_name = serializers.CharField(max_length=256, required=False)

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = validated_data.get('slug')
        parent_name = validated_data.get('parent_name', None)

        if parent_name is not None:
            parent = get_object_or_404(Category, is_active=True, name=parent_name)
            category = Category.objects.create(name=name, slug=slug, parent=parent)
        else:
            category = Category.objects.create(name=name, slug=slug)

        return category

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        slug = validated_data.get('slug', instance.slug)
        parent_name = validated_data.get('parent_name', None)

        if parent_name is not None:
            category = get_object_or_404(Category, name=parent_name)
            instance.parent = category

        instance.name = name
        instance.slug = slug

        instance.save()
        return instance


class ProductSpecificationListSerializer(serializers.ModelSerializer):
    """
    show product_specification object
    """

    class Meta:
        model = ProductType
        fields = ('pk', 'name')


class ProductTypeDetailSerializer(serializers.ModelSerializer):
    """
    show product_type object and product specification list for that
    """
    typed_product = ProductSpecificationListSerializer(many=True)

    class Meta:
        model = ProductType
        fields = ('pk', 'name', 'typed_product')


class ProductTypeSerializer(serializers.ModelSerializer):
    """
    show product_type object
    """

    class Meta:
        model = ProductType
        fields = ('pk', 'name')


class ProductTypeInputSerializer(serializers.ModelSerializer):
    """
    create,update product_type object
    """

    class Meta:
        model = ProductType
        fields = ('name', 'is_active',)


class ProductSpecialInputSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    product_type_name = serializers.CharField(max_length=256, required=True)

    def create(self, validated_data):
        """
        create object by name and product_type_name
        if dont exist product_type_name ==> error 404
        """
        name = validated_data.get('name')
        product_type_name = validated_data.get('product_type_name')

        product_type = get_object_or_404(ProductType, is_active=True, name=product_type_name)
        product_special = ProductSpecification.objects.create(name=name, product_type=product_type)
        return product_special

    def update(self, instance, validated_data):
        """
        update product special object by product_type name
        find object by product_type name
        update name object
        if dont exist product_type_name ==> error 404
        """
        name = validated_data.get('name')
        product_type_name = validated_data.get('product_type_name')

        product_type = get_object_or_404(ProductType, name=product_type_name, is_active=True)
        instance.name = name
        instance.product_type = product_type

        instance.save()
        return instance
