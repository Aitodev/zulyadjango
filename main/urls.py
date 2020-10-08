from django.urls import path, include
from .views import *
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_product>', views.product, name='product'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]