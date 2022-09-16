from django.db import models
import datetime

def get_default_date() -> datetime.date:
    return datetime.datetime.now().date()

class Tenant(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    create_at = models.DateField(auto_created=True, default=get_default_date)
    updated_at = models.DateField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    product_name = models.CharField(max_length=32)
    product_slug = models.SlugField(max_length=32)
    product_description = models.TextField(null=True, blank=True)
    product_cost = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=False)


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    category_slug = models.SlugField(max_length=32)
    category_description = models.TextField(null=True, blank=True)