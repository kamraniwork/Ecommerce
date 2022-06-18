from django.contrib.auth import get_user_model
from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import ProductType


class ProductTypeTestCase(BaseTest):

    def test_list_product_type(self):
        """ Test list product_type """

        res = self.client.get(reverse('product:product-type-list'))
        category = ProductType.objects.all().count()

        self.assertEqual(category, 1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_product_type(self):
        """ Test just user can create product_type objects """

        self.client.force_authenticate(user=self.user)

        response = self.client.post('/product-type/', data={
            'name': 'color',
        })

        self.assertEqual(ProductType.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_create_product_type(self):
        """ Test just superuser can create category objects """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/product-type/', data={
            'name': 'color'
        })
        self.assertEqual(ProductType.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_invalid_create_product_type(self):
        """ Test dont create object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/product-type/', data={
            'names': 'color'
        })
        self.assertEqual(ProductType.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product_type(self):
        """ Test update product_type by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-type-detail', args=[ProductType.objects.first().pk])
        res = self.client.put(url, {
            'name': 'color'
        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductType.objects.first().name, 'color')

    def test_update_product_type_by_user(self):
        """ Test update product_type by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-type-detail', args=[ProductType.objects.first().pk])
        res = self.client.put(url, {
            'name': 'color'
        })

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductType.objects.first().name, 'size')

    def test_serializer_invalid_update_product_type(self):
        """ Test dont update object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-type-detail', args=[ProductType.objects.first().pk])
        res = self.client.put(url, {
            'names': 'color'
        })
        self.assertEqual(ProductType.objects.first().name, "size")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product_type(self):
        """ Test delete product_type by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-type-detail', args=[ProductType.objects.first().pk])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductType.objects.all().count(), 0)

    def test_delete_product_type_by_user(self):
        """ Test delete product_type by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-type-detail', args=[ProductType.objects.first().pk])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductType.objects.all().count(), 1)
