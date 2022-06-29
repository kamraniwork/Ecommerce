from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from product.models import ProductType, Category, ProductSpecification, Product, ProductSpecificationValue, ProductImage
import PIL
from django.core.files.uploadedfile import tempfile
from django.core.files import File
import os
from django.conf import settings

User = get_user_model()


class BaseTest(APITestCase):
    """
    Base test case
    """
    client = APIClient
    token = ''

    def setUp(self):
        """
        setup test data
        """
        self.category_main = Category.objects.create(name='django', slug='django')
        self.superuser = User.objects.create_superuser(username="mehran", email="m@gmail.com", password="1234")
        self.user = User.objects.create_user(username="ali", email="m2@gmail.com", password="1234")
        self.product_type_main = ProductType.objects.create(name="book")
        self.product_special_main = ProductSpecification.objects.create(name='pages',
                                                                        product_type=self.product_type_main)
        self.product_main = Product.objects.create(title="django by example", product_type=self.product_type_main,
                                                   category=self.category_main, slug="djexample", regular_price=100.00,
                                                   discount_price=80.00)

        self.special_value_main = ProductSpecificationValue.objects.create(
            product=self.product_main,
            specification=self.product_special_main,
            value="500"
        )

        image = PIL.Image.new('RGB', size=(1, 1))
        self.file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(self.file)
        fn = os.path.join(settings.MEDIA_ROOT, 'images', 'test.jpg')
        img = ProductImage(product=self.product_main, alt_text="main image")
        with open(fn, encoding="utf8", errors='ignore') as f:
            img.image.save(fn, f)
