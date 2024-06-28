from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import uuid

from account.service.account_service_impl import AccountServiceImpl
from kakao_oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakao_oauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakao_oauth.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
from kakao_oauth.service.redis_service_impl import RedisServiceImpl

# Create your views here.
class KakaoOauthView(viewsets.ViewSet):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def kakaoOauthURI(self, request):
        url = self.kakaoOauthService.kakaoLoginAddress()

        serializer = KakaoOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def kakaoAccessTokenURI(self, request):
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse(accessToken, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({ 'error': str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def kakaoUserInfoURI(self, request):
        accessToken = request.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            user_info = self.kakaoOauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)




    def redisAccessToken(self, request):
        try:
            email = request.data.get('email')
            # TODO: 처음에 좀 비몽사몽한 상태로 만들어서 쓸대없이 accessToken 넣었으나 필요 없음
            #       향후 로직에서 제거할 필요가 있음 (일단 되게 만들기)
            #       토큰 탈취 시 카카오 계정까지 털려버림
            access_token = request.data.get('accessToken')
            print(f"redisAccessToken -> email: {email}")

            account = self.accountService.findAccountByEmail(email)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            userToken = str(uuid.uuid4())
            self.redisService.store_access_token(account.id, userToken)
            # key로 value 찾기 테스트
            accountId = self.redisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            return Response({ 'userToken': userToken }, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)

            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print('래디스 토큰 해제 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)