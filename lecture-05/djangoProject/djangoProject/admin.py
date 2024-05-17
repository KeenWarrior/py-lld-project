from django.contrib import admin
from djangoProject.models import User, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'username', 'name', 'email']
    list_display = ['id', 'username', 'name']
    search_fields = ['id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['id']
    save_as = True
    fieldsets = (
        ("Product Info", {
            'fields': ('seller', 'name', 'description')
        }),
        ("Stock Info", {
            'fields': ('price', 'stock'),
            'classes': ('collapse',)
        })
    )




