from django.shortcuts import render
from rest_framework import viewsets, status
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

    def register(self, request):
        try:
            data = request.data

            productImageName = request.FILES.get('productImageName')
            productName = data.get('productName')
            productLocation = data.get('productLocation')
            productActivity = data.get('productActivity')
            productDining = data.get('productDining')
            productPrice = data.get('productPrice')

            if not all([productImageName, productName, productLocation, productActivity, productDining, productPrice]):
                return Response({ 'error': '모든 내용을 채워주세요!' },
                                status=status.HTTP_400_BAD_REQUEST)

            self.productService.createProduct(productName, productLocation, productActivity, productDining, productPrice, productImageName)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('호텔 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e) },
                            status=status.HTTP_400_BAD_REQUEST)
