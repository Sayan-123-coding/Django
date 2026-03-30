from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'myApp/app.html')

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')