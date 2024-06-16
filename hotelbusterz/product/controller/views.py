from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from product.entity.models import Product
from product.service.product_service_impl import ProductServiceImpl
from product.serializers import ProductSerializer


# Create your views here.
class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    productService = ProductServiceImpl.getInstance()

    def list(self, request):
        productList = self.productService.list()
        serializer = ProductSerializer(productList, many=True)
        return Response(serializer.data)
