from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kakao_oauth.controller.views import KakaoOauthView

router = DefaultRouter()

router.register(r'kakaoOauth', KakaoOauthView, basename='kakaoOauth')

urlpatterns = [
    path('', include(router.urls)),
    path('kakao', KakaoOauthView.as_view({'get': 'kakaoOauthURI'}), name='get-kakao-oauth-uri'),
    path('kakao/access-token', KakaoOauthView.as_view({'post': 'kakaoAccessTokenURI'}), name='get-kakao-access-token-uri'),
    path('kakao/user-info', KakaoOauthView.as_view({'post': 'kakaoUserInfoURI'}), name='get-kakao-user-info-uri'),
    path('redis-access-token/', KakaoOauthView.as_view({'post': 'redisAccessToken'}),
         name='redis-access-token'),
    path('logout', KakaoOauthView.as_view({'post': 'dropRedisTokenForLogout'}),
         name='drop-redis-token-for-logout'),
]