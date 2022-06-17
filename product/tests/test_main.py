from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from product.models import Product, Category

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
