from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fiels = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone', 'address', 'city', 'delivery_way', 'comment', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
