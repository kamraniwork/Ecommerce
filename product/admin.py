from django.contrib import admin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'slug')
    list_filter = (['name'])
    search_fields = ('name', 'slug')
    list_editable = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
