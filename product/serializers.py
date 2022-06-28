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
    Product,
    ProductSpecificationValue
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


class ProductSpecialValueSerializer(serializers.ModelSerializer):
    """
    show list objects
    """

    class Meta:
        model = ProductSpecificationValue
        fields = ('pk', 'value')


class ProductSpecificationListSerializer(serializers.ModelSerializer):
    """
    show product_specification object
    """

    special_value_product = ProductSpecialValueSerializer(many=True)

    class Meta:
        model = ProductSpecification
        fields = ('pk', 'name', 'special_value_product')


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


class ProductSpecialListSerializer(serializers.ModelSerializer):
    """
    show list objects
    """

    class Meta:
        model = ProductSpecification
        fields = ('pk', 'name')


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


class ProductListSerializer(serializers.ModelSerializer):
    """
    show list products
    """

    class Meta:
        model = Product
        fields = ('title', 'slug', 'regular_price', 'discount_price', 'updated_at',)


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    show product object
    """
    product_type = ProductTypeDetailSerializer()
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'title', 'description', 'product_type', 'category', 'slug', 'regular_price',
            'discount_price',
            'updated_at',)


class ProductInputSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=256, required=True)
    description = serializers.CharField(max_length=1000)
    slug = serializers.SlugField(max_length=50)
    regular_price = serializers.DecimalField(max_digits=5, decimal_places=2, required=True)
    discount_price = serializers.DecimalField(max_digits=5, decimal_places=2, required=True)
    is_active = serializers.BooleanField(default=False)
    product_type_name = serializers.CharField(max_length=256, required=True)
    category_name = serializers.CharField(max_length=256, required=True)

    def create(self, validated_data):
        """
        create object by product_type_name and category_name
        if dont exist product_type_name or category_name ==> error 404
        """
        title = validated_data.get('title')
        description = validated_data.get('description', None)
        slug = validated_data.get('slug')
        regular_price = validated_data.get('regular_price')
        discount_price = validated_data.get('discount_price')
        is_active = validated_data.get('is_active')
        product_type_name = validated_data.get('product_type_name')
        category_name = validated_data.get('category_name')

        product_type = get_object_or_404(ProductType, is_active=True, name=product_type_name)
        category = get_object_or_404(Category, is_active=True, name=category_name)
        product = Product.objects.create(title=title, product_type=product_type, category=category,
                                         description=description, regular_price=regular_price,
                                         discount_price=discount_price,
                                         is_active=is_active, slug=slug)
        return product

    def update(self, instance, validated_data):
        """
        update product object by product_type_name or category_name or other fields
        find object by product_type name
        if dont exist product_type_name ==> error 404
        """
        title = validated_data.get('title', instance.title)
        description = validated_data.get('description', instance.description)
        slug = validated_data.get('slug', instance.slug)
        regular_price = validated_data.get('regular_price', instance.regular_price)
        discount_price = validated_data.get('discount_price', instance.discount_price)
        is_active = validated_data.get('is_active', instance.is_active)
        product_type_name = validated_data.get('product_type_name')
        category_name = validated_data.get('category_name')

        product_type = get_object_or_404(ProductType, is_active=True, name=product_type_name)
        category = get_object_or_404(Category, is_active=True, name=category_name)

        instance.product_type = product_type
        instance.category = category
        instance.title = title
        instance.description = description
        instance.slug = slug
        instance.regular_price = regular_price
        instance.discount_price = discount_price
        instance.is_active = is_active

        instance.save()
        return instance


class ProductSpecialValueInputSerializers(serializers.Serializer):
    value = serializers.CharField(max_length=256, required=True)
    product_slug = serializers.CharField(max_length=256, required=True)
    specification_name = serializers.CharField(max_length=256, required=True)

    def create(self, validated_data):
        """
        create object by value and product_name and specification_name
        if dont exist product_name ==> error 404
        """
        value = validated_data.get('value')
        product_slug = validated_data.get('product_slug')
        specification_name = validated_data.get('specification_name')

        product = get_object_or_404(Product, is_active=True, slug=product_slug)
        product_special = get_object_or_404(ProductSpecification, name=specification_name)
        product_special_value = ProductSpecificationValue.objects.create(value=value, product=product,
                                                                         specification=product_special)
        return product_special_value

    def update(self, instance, validated_data):
        """
        update product special value object by pk
        find object by product_special_value pk
        update value object
        """
        value = validated_data.get('value')
        product_slug = validated_data.get('product_slug')
        specification_name = validated_data.get('specification_name')

        product = get_object_or_404(Product, slug=product_slug, is_active=True)
        specification = get_object_or_404(ProductSpecification, name=specification_name)

        instance.value = value
        instance.specification = specification
        instance.product = product

        instance.save()
        return instance
