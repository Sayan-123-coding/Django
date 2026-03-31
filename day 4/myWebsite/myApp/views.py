from django.shortcuts import render
from .models import Product


# Create your views here.
def app(request):
    products = Product.objects.all()
    return render(request, 'myApp/app.html', {'products': products})

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')