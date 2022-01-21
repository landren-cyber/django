from django.db import models
from test_app.models import Product

class Order(models.Model):
    DELIVERY_CHOICES = [
        ('FREE', 'Бесплатная доставка'),
        ('SELF', 'Самовывоз'),
        ('PAID', 'Доставка с оплатой'),
    ]
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    delivery_way = models.CharField(max_length=4, choices=DELIVERY_CHOICES, default='FREE',)
    comment = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
