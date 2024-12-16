from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    product = get_object_or_404(Product, id=product_id)
    product_variation = []

    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(
                    product=product, 
                    variation_category__iexact=key, 
                    variation_value__iexact=value
                )
                product_variation.append(variation)
            except Variation.DoesNotExist:
                continue

    # If the user is authenticated
    if current_user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=current_user,
            defaults={'quantity': 0}
        )
        if created:
            cart_item.quantity = 1
            cart_item.variations.add(*product_variation)
        else:
            cart_item.quantity += 1
            cart_item.save()
            if product_variation:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
        cart_item.save()
        return redirect('cart')

    # If the user is not authenticated
    else:
        cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
        cart.save()

        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            cart=cart,
            defaults={'quantity': 0}
        )
        if created:
            cart_item.quantity = 1
            cart_item.variations.add(*product_variation)
        else:
            cart_item.quantity += 1
            cart_item.save()
            if product_variation:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
        cart_item.save()
        return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

def get_cart_items_and_totals(request):
    total = 0
    quantity = 0
    cart_items = []

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
    
        cart_id = _cart_id(request)
        cart, created = Cart.objects.get_or_create(cart_id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2 * total) / 100 
    grand_total = total + tax

    return cart_items, total, quantity, tax, grand_total

def cart(request):
    cart_items, total, quantity, tax, grand_total = get_cart_items_and_totals(request)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request):
    cart_items, total, quantity, tax, grand_total = get_cart_items_and_totals(request)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)
