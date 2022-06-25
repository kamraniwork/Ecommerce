from django.contrib.auth import get_user_model
from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import ProductType, ProductSpecification


class ProductSpecialTestCase(BaseTest):

    def test_create_product_special(self):
        """ Test just user can create product_special objects """

        self.client.force_authenticate(user=self.user)

        response = self.client.post('/product-specification/', data={
            'name': 'color',
            'product_type_name': 'book'

        })

        self.assertEqual(ProductSpecification.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_create_product_special(self):
        """ Test just superuser can create product_special objects """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/product-specification/', data={
            'name': 'color',
            'product_type_name': 'book'

        })
        self.assertEqual(ProductSpecification.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_invalid_create_product_special(self):
        """ Test dont create object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/product-specification/', data={
            'names': 'color',
            'product_type_name': 'book'

        })
        self.assertEqual(ProductSpecification.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product_special(self):
        """ Test update product_special by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-specification-detail', args=[ProductSpecification.objects.first().name])
        res = self.client.put(url, {
            'name': 'color',
            'product_type_name': 'book'

        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductSpecification.objects.first().name, 'color')

    def test_update_product_special_by_user(self):
        """ Test update product_special by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-specification-detail', args=[ProductSpecification.objects.first().name])
        res = self.client.put(url, data={
            'names': 'color',
            'product_type_name': 'book'

        })

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductSpecification.objects.first().name, 'pages')

    def test_serializer_invalid_update_product_special(self):
        """ Test dont update object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-specification-detail', args=[ProductSpecification.objects.first().name])
        res = self.client.put(url, {
            'names': 'color'
        })
        self.assertEqual(ProductSpecification.objects.first().name, "pages")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product_special(self):
        """ Test delete product_special by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:product-specification-detail', args=[ProductSpecification.objects.first().name])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductSpecification.objects.all().count(), 0)

    def test_delete_product_special_by_user(self):
        """ Test delete product_special by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:product-specification-detail', args=[ProductSpecification.objects.first().name])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductSpecification.objects.all().count(), 1)
