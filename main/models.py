from django.db import models
from django.contrib import admin


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=750)
    price = models.FloatField()
    image = models.ImageField(upload_to="uploads/")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.product_name

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % self.image)

    image_tag.short_description = 'Image'


class Newsletter(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
