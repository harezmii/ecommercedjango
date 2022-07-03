from django.contrib import admin
from .models import Category, Product , Newsletter


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "sub_category_id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category_id", "image_tag", "created_at", "status")
    list_filter = ("status",)
    search_fields = ("product_name",)


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = ("name", "email")


admin.site.site_header = "E Ticaret Admin Panel"
