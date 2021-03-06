from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from test_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from orders.forms import OrderCreateForm

def cart_detail(request):
    cart = Cart(request)
    form = OrderCreateForm()
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'cart_product_form': cart_product_form, 'form': form})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')
