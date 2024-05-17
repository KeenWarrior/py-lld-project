from django.contrib import admin
from djangoProject.models import User, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email']
    list_display = ['id', 'username', 'name']
    search_fields = ['id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description', 'stock']
    list_display = ['id', 'name', 'price']
    search_fields = ['id']




