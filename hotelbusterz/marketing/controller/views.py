from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from marketing.service.marketing_service_impl import MarketingServiceImpl


# Create your views here.
class MarketingView(viewsets.ViewSet):
    marketingService = MarketingServiceImpl.getInstance()

    def marketingList(self, request):
        self.marketingService.createMarketingData()
        return Response(status=status.HTTP_200_OK)