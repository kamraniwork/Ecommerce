from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from product.models import ProductType, Category, ProductSpecification

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
