from django.db import models


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(parent__isnull=True, is_active=True)
