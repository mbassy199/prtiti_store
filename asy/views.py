from django.shortcuts import render
from store.models import Product

def home(request):
    # Get the most recent creation date from available products
    latest_product = Product.objects.filter(is_available=True).order_by('-created_date').first()
    latest_date = latest_product.created_date.date() if latest_product else None

    # Filter products by the most recent date
    products = Product.objects.filter(is_available=True, created_date__date=latest_date).order_by('-created_date')[:10] if latest_date else []

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
