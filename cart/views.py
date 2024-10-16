from django.shortcuts import redirect, render , get_object_or_404
from .cart import Cart
from shop.models import Product
# Create your views here.

def cart_add(requset,product_id):
    cart = Cart(requset)
    product = get_object_or_404(Product, id=product_id)


    size = requset.POST.get("size")
    quantity = int(requset.POST.get("quantity", 1))

    requset.session['last_quantity'] = quantity
    requset.session['last_size'] = size


    cart.add(product=product, quantity=quantity, size=size)
    return redirect("cart:cart_detail")

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_summary.html', {'cart': cart})