from django.contrib import admin
from aplication.models import Tenant, Product, Category
# Register your models here.

class TenantModelAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'is_active'
    list_display_links = 'first_name', 'last_name'
    list_filter = 'is_active', 'last_name'

class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'product_name', 'product_cost', 'availability', 'product_slug'
    list_editable = 'product_cost', 'availability', 'product_slug'
    list_filter = 'product_cost', 'availability'
    prepopulated_fields = {
        'product_slug': ['product_name']
    }

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = 'category_name', 'category_slug'
    list_filter = ['category_name']
    prepopulated_fields = {
        'category_slug': ['category_name']
    }

admin.site.register(Tenant, TenantModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)

