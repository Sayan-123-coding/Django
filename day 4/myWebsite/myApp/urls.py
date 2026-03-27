from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='myapp_home'),
    path('app/', views.app, name='app'),
]
