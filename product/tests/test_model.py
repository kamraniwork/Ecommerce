from django.contrib.auth import get_user_model
from django.test import TestCase

from product.models import Category, Product, ProductType, ProductSpecification, ProductSpecificationValue

User = get_user_model()


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        count_category = Category.objects.count()
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')
        self.assertEqual(count_category, 1)


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        ProductType.objects.create(name='book', is_active=True)
        ProductSpecification.objects.create(product_type_id=1, name='author')

        self.data1 = Product.objects.create(category_id=1, product_type_id=1, title='django beginners',
                                            slug='django-beginners', regular_price='20.00', discount_price=20.00,
                                            is_active=True)

        ProductSpecificationValue.objects.create(product_id=1, specification_id=1, value='arastoo')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.objects.all()
        self.assertEqual(data.count(), 1)
