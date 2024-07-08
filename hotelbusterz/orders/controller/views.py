from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from kakao_oauth.service.redis_service_impl import RedisServiceImpl
from orders.entity.orders import Orders
from orders.service.orders_service_impl import OrdersServiceImpl


class OrdersView(viewsets.ViewSet):
    queryset = Orders.objects.all()
    ordersService = OrdersServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createOrders(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            productId = data.get('productId')

            orderId = self.ordersService.createOrder(accountId, productId)
            print(f"controller -> createOrders() orderId: {orderId}")
            return Response(orderId, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def readOrders(self, request, ordersId):
        try:
            data = request.data
            print(f"readOrders data: {data}")
            print(f'data: {data}, ordersId: {ordersId}')

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            if not accountId:
                raise ValueError('Invalid userToken')

            orders = self.ordersService.readOrderDetails(ordersId, accountId)

            return Response(orders, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 상세 내역 조회 중 문제 발생:', e)
            return Response({ 'error': str(e) }, status=status.HTTP_400_BAD_REQUEST)

    def ordersList(self, request):
        try:
            data = request.data
            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            if not accountId:
                raise ValueError('Invalid userToken')

            ordersList = self.ordersService.ordersList(accountId)

            return Response(ordersList, status=status.HTTP_200_OK)

        except Exception as e:
            print('주문 리스트 조회 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)