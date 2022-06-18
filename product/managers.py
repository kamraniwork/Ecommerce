from django.db import models


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(parent__isnull=True, is_active=True)


class ProductTypeManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)
