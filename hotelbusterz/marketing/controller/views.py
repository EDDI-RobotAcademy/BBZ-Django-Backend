from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from marketing.entity.models import Marketing
from marketing.service.marketing_service_impl import MarketingServiceImpl


# Create your views here.
class MarketingView(viewsets.ViewSet):
    marketingService = MarketingServiceImpl.getInstance()

    def marketingList(self, request):
        self.marketingService.createMarketingData()
        total_data = self.marketingService.createtotalAARRR(Marketing.objects.all())

        return JsonResponse(total_data)