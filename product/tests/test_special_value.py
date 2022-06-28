from django.contrib.auth import get_user_model
from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import ProductType, ProductSpecification, Product, ProductSpecificationValue


class ProductSpecialValueTestCase(BaseTest):

    def test_create_product_special_value(self):
        """ Test user can not create product_special_value objects """

        self.client.force_authenticate(user=self.user)

        response = self.client.post('/special-value/', data={
            "specification_name": "pages",
            "value": "500",
            "product_slug": "djexample"
        })

        self.assertEqual(ProductSpecification.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_create_product_special_value(self):
        """ Test just superuser can create product_special_value objects """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/special-value/', data={
            "specification_name": "pages",
            "value": "500",
            "product_slug": "djexample"

        })
        self.assertEqual(ProductSpecificationValue.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_invalid_create_product_special_value(self):
        """ Test dont create object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        # value is correct
        response = self.client.post('/special-value/', data={
            "specification_name": "pages",
            "vlaue": "500",
            "product_slug": "djexample"

        })
        self.assertEqual(ProductSpecificationValue.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product_special_value(self):
        """ Test update product_special_value by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:special-value-detail', args=[ProductSpecificationValue.objects.first().pk])
        res = self.client.put(url, {
            "specification_name": "pages",
            "value": "900",
            "product_slug": "djexample"

        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductSpecificationValue.objects.first().value, '900')

    def test_update_product_special_value_by_user(self):
        """ Test update product_special_value by user """

        self.client.force_authenticate(user=self.user)

        url = reverse('product:special-value-detail', args=[ProductSpecificationValue.objects.first().pk])
        res = self.client.put(url, data={
            "specification_name": "pages",
            "value": "900",
            "product_slug": "djexample"
        })

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductSpecificationValue.objects.first().value, '500')

    def test_serializer_invalid_update_product_special_value(self):
        """ Test dont update object if invalid serializer """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:special-value-detail', args=[ProductSpecificationValue.objects.first().pk])
        # value is correct
        res = self.client.put(url, {
            "specification_name": "pages",
            "vlaue": "900",
            "product_slug": "djexample"
        })
        self.assertEqual(ProductSpecificationValue.objects.first().value, "500")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product_special_value(self):
        """ Test delete product_special_value by superuser """

        self.client.force_authenticate(user=self.superuser)
        self.assertEqual(ProductSpecificationValue.objects.all().count(), 1)

        url = reverse('product:special-value-detail', args=[ProductSpecificationValue.objects.first().pk])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductSpecificationValue.objects.all().count(), 0)

    def test_delete_product_special_value_by_user(self):
        """ Test delete product_special by user """


        self.assertEqual(ProductSpecificationValue.objects.all().count(), 1)
        self.client.force_authenticate(user=self.user)

        url = reverse('product:special-value-detail', args=[ProductSpecificationValue.objects.first().pk])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductSpecification.objects.all().count(), 1)
