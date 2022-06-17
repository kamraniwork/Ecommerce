from django.db import models


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)
