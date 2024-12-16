from .models import CartItem
from django.contrib import messages

def transfer_guest_cart_to_user(request):
    """Transfer guest cart items to the authenticated user's cart."""
    if request.user.is_authenticated:
        cart_id = _cart_id(request)
        guest_cart_items = CartItem.objects.filter(cart__cart_id=cart_id)

        for item in guest_cart_items:
            # Check if the product still exists before transferring
            if item.product.exists():
                cart_item, created = CartItem.objects.get_or_create(
                    product=item.product,
                    user=request.user,
                    defaults={'quantity': item.quantity}
                )
                if not created:
                    cart_item.quantity += item.quantity
                    cart_item.save()
                item.delete()
                messages.info(request, f"Transferred {item.product.product_name} to {request.user.username}'s cart.")
            else:
                messages.warning(request, f"The product {item.product.product_name} no longer exists.")
