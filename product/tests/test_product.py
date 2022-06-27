from django.contrib.auth import get_user_model
from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import Product


class ProductTypeTestCase(BaseTest):

    def test_list_product(self):
        """ Test list product """

        res = self.client.get(reverse('product:product-list'))
        category = Product.objects.all().count()

        self.assertEqual(category, 1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        """ Test just user can not create product objects """

        self.client.force_authenticate(user=self.user)

        response = self.client.post('/product/', data={
            "title": "django by example",
            "slug": "djexample",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })

        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_create_product(self):
        """ Test just superuser can create product objects """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/product/', data={
            "title": "django by example",
            "slug": "djexample",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })
        self.assertEqual(Product.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_invalid_create_product(self):
        """ Test dont create object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        # titel is wrong
        response = self.client.post('/product/', data={
            "titel": "django by example",
            "slug": "djexample",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product(self):
        """ Test update product_type by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-detail', args=[Product.objects.first().slug])
        res = self.client.put(url, {
            "title": "two scoop of django",
            "slug": "twoscoop",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.first().title, 'two scoop of django')

    def test_update_product_by_user(self):
        """ Test update product by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-detail', args=[Product.objects.first().slug])
        res = self.client.put(url, {
            "title": "two scoop of django",
            "slug": "twoscoop",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.first().title, 'django by example')

    def test_serializer_invalid_update_product(self):
        """ Test dont update object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-detail', args=[Product.objects.first().slug])

        # titel is wrong
        res = self.client.put(url, {
            "titel": "two scoop of django",
            "slug": "twoscoop",
            "description": "good",
            "discount_price": "100.00",
            "regular_price": "80.00",
            "product_type_name": "book",
            "category_name": "django",
            "is_active": "true"
        })
        self.assertEqual(Product.objects.first().title, "django by example")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product(self):
        """ Test delete product by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-detail', args=[Product.objects.first().slug])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.all().count(), 0)

    def test_delete_product_by_user(self):
        """ Test delete product by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-detail', args=[Product.objects.first().slug])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.all().count(), 1)
