from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.controller.views import SurveyView

router = DefaultRouter()
router.register(r'survey', SurveyView)


urlpatterns = [
    path('', include(router.urls)),
    path('register', SurveyView.as_view({'post': 'register'}), name='survey-register'),
]