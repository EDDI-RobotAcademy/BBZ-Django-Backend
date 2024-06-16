from django.shortcuts import render
from rest_framework import viewsets

from product.entity.models import Product
from product.service.product_service_impl import ProductServiceImpl


# Create your views here.
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()