from django.contrib.auth import get_user_model
from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import Product, Category


class CategoryTestCase(BaseTest):

    def test_list_category(self):
        """ Test list category """

        res = self.client.get(reverse('product:category-list'))
        category = Category.objects.all().count()

        self.assertEqual(category, 1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        """ Test just user can create category objects """

        self.client.force_authenticate(user=self.user)

        response = self.client.post('/category/', data={
            'name': 'mobile',
            'slug': 'mobile'
        })

        self.assertEqual(Category.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_superuser_create_category(self):
        """ Test just superuser can create category objects """

        self.client.force_authenticate(user=self.superuser)

        response = self.client.post('/category/', data={
            'name': 'mobile',
            'slug': 'mobile'
        })
        self.assertEqual(Category.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        """ Test update category by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:category-detail', args=[Category.objects.first().slug])
        res = self.client.put(url, {
            'name': 'phone',
            'slug': 'phone'
        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.first().name, 'phone')

    def test_delete_category(self):
        """ Test delete category by superuser """

        self.client.force_authenticate(user=self.superuser)

        url = reverse('product:category-detail', args=[Category.objects.first().slug])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.all().count(), 0)
