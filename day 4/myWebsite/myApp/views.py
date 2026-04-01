from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def app(request):
    products = Product.objects.all()
    return render(request, 'myApp/app.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myApp/product_details.html', {'product': product})

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')