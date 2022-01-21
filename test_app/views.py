from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from .models import Product, Category
from cart.forms import CartAddProductForm

def index(request):
    products = Product.objects.all()
    return render(request, 'test_app/index.html', {'products':products})

def product(request):
    return render(request, 'test_app/productdetail.html', {})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
        id=id,
        slug=slug,
        available=True,)
    cart_product_form = CartAddProductForm()
    return render(request, 'test_app/productdetail.html', {'product': product, 'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(Q(category=category) | Q(category__parent=category))
    else:
        products = products[:12]
    return render(request, 'test_app/catalog.html', {'category':category,
                                                    # 'categories':categories,
                                                    'products':products,
                                                    })
