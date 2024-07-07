from django.shortcuts import render
from rest_framework import viewsets

from marketing.entity.models import Marketing


# Create your views here.
class MarketingView(viewsets.ViewSet):
    queryset = Marketing.objects.all()
