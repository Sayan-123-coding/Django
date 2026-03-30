from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.app, name='app'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
