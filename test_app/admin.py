from django.contrib import admin
from .models import Category, Product, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'created', 'available', 'updated']
    list_filter = [ 'created', 'updated', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
