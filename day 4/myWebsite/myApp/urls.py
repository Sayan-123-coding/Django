from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.app, name='app'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
