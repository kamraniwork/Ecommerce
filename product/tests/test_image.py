from .test_main import BaseTest
from rest_framework import status
from django.urls import reverse
from ..models import ProductImage
import PIL
from django.core.files.uploadedfile import tempfile
from django.shortcuts import get_object_or_404


class CategoryTestCase(BaseTest):
    def test_image_upload(self):
        """ Test image upload"""
        self.client.force_authenticate(user=self.superuser)
        with open(self.file.name, 'rb') as f:
            data = {
                "image": f,
                "product_slug": "djexample",
                "alt_text": "main image"
            }
            response = self.client.post(reverse('product:images-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductImage.objects.all().count(), 2)

    def test_image_upload_user(self):
        """ Test dont create object by user"""
        self.client.force_authenticate(user=self.user)
        with open(self.file.name, 'rb') as f:
            data = {
                "image": f,
                "product_slug": "djexample",
                "alt_text": "main image"
            }
            response = self.client.post(reverse('product:images-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(ProductImage.objects.all().count(), 1)

    def test_delete_image(self):
        """Test delete image"""
        self.client.force_authenticate(user=self.superuser)

        self.assertEqual(ProductImage.objects.all().count(), 1)
        self.client.delete(reverse("product:images-detail", args=[1]))
        self.assertEqual(ProductImage.objects.all().count(), 0)

    def test_delete_image_user(self):
        """Test dont delete image by user"""
        self.client.force_authenticate(user=self.user)

        self.assertEqual(ProductImage.objects.all().count(), 1)
        self.client.delete(reverse("product:images-detail", args=[1]))
        self.assertEqual(ProductImage.objects.all().count(), 1)
