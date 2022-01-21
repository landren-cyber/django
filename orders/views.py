import json
from django.shortcuts import render, HttpResponse
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
from .telegram import send_message
from django.core.mail import send_mail

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            product_positions = ''
            client_name = request.POST.get('first_name', False)
            client_phone = request.POST.get('phone', False)
            client_delivery = request.POST.get('delivery_way', False)
            for item in cart:
                product_positions+='{} x {}\n'.format(item['product'].name, item['quantity'])
                order_item = OrderItem(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                order_item.save()
            send_message('Получен заказ: \n {} \n {} \n {} \n {}'.format(client_name, client_phone, client_delivery, product_positions))
            send_mail(
                'Заказ',
                'Получен заказ на: \n {} \n {} \n {} \n {}'.format(client_name, client_phone, client_delivery, product_positions),
                'skyline2029@vivaldi.net',
                ['skyline2029@vivaldi.net'],
                fail_silently=False,
            )
            cart.clear()
            return render(request, 'orders/thankyoupage.html',
                                    {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/thankyoupage.html',
                            {'cart': cart, 'form': form})
