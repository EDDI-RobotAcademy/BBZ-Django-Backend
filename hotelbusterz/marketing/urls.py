from django.urls import path, include
from rest_framework.routers import DefaultRouter

from marketing.controller.views import MarketingView

router = DefaultRouter()
router.register(r'marketing', MarketingView)

urlpatterns = [
    path('',  include(router.urls)),
]
