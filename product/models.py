from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
                       ┌─────────────────────────┐
                       │                         │
                       │                       ┌─┼─┐
                  ┌────┴────────┐         ┌────┴─┼─┴───┐
                  │    neme     │         │      │     │
     xxxxx  xxxx  │             │         │            │   xxxxxx  xxxxx
    xx   xxxx  xx │    slug     │         │            │  xx    xxxx xxxx
    xx    xx    x │             │         │            │  xx    xx    x x
     x         xx │    is_active│         │   product  │   xx         xxx
      xx      xx  │             │         │            │    xx       xxx
       xxx   xx   │    parent   │         │            │     xxx    xxx
         xxxx     │             │         │            │       xxxxxxx
                  │             │         │            │         xxx
                  │             │         │            │
                  └─────────────┘         └────────────┘
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_("Category safe URL"),
        max_length=255,
        unique=True
    )
    parent = models.ManyToManyField(
        "self",
        blank=True,
        related_name="children"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
         ┌─────────────────────┐
         │                     │
         │                   ┌─┼─┐
    ┌────┴────────┐      ┌───┴─┼─┴────┐
    │             │      │     │      │
    │   name      │      │            │
    │             │      │            │
    │             │      │  product   │
    │   is_active │      │            │
    │             │      │            │
    │             │      │            │
    │             │      │            │
    │             │      │            │
    │             │      │            │
    └─────────────┘      └────────────┘
    """

    name = models.CharField(
        verbose_name=_("Product Name"),
        help_text=_("Required"),
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
                     ┌─────────────────────┐
                     │                     │
                     │                   ┌─┼─┐
                ┌────┴────────┐      ┌───┴─┼─┴────┐
                │             │      │     │      │
                │ name        │      │            │   ┌────────┐
    ┌────────┐  │             │      │            │   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │ product_type│      │    product │   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │             │      │            │   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │             │      │   specifica│   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │             │      │            │   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │             │      │   tion     │   │┼┼┼┼┼┼┼┼│
    │┼┼┼┼┼┼┼┼│  │             │      │            │   └────────┘
    └────────┘  │             │      │            │
                └─────────────┘      └────────────┘
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Required"),
        max_length=255
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Not Required"),
        blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, null=True, on_delete=models.SET_NULL)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
         ┌─────────────────────┐
         │                     │
         │                   ┌─┼─┐
    ┌────┴────────┐      ┌───┴─┼─┴────┐
    │             │      │     │      │
    │             │      │  product   │
    │             │      │            │
    │    product  │      │  image     │
    │             │      │            │
    │             │      │  alt_text  │
    │             │      │            │
    │             │      │  is_feature│
    │             │      │            │
    │             │      │  create_at │
    └─────────────┘      └────────────┘
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
