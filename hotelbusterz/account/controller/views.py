from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from kakao_oauth.service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        # url = self.oauthService.kakaoLoginAddress()
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재' \
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkNicknameDuplication(self, request):
        print("checkNicknameDuplication()")

        try:
            nickname = request.data.get('newNickname')
            print(f"nickname: {nickname}")
            isDuplicate = self.accountService.checkNicknameDuplication(nickname)

            return Response({'isDuplicate': isDuplicate, 'message': 'Nickname이 이미 존재' \
                             if isDuplicate else 'Nickname 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def registerAccount(self, request):
        try:
            nickname = request.data.get('nickname')
            email = request.data.get('email')

            account = self.accountService.registerAccount(
                loginType='KAKAO',
                roleType='NORMAL',
                nickname=nickname,
                email=email,
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def registerLog(self, request):
        try:
            userToken = request.data.get('userToken')

            accountId = self.redisService.getValueByKey(userToken)

            if accountId is None:
                return Response(status=status.HTTP_200_OK)
            action = request.data.get('actionType')
            actionTime = request.data.get('actionTime')

            log = self.accountService.registerLog(
                accountId=accountId,
                action=action,
                actionTime=actionTime,
            )

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("로그 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def getNickname(self, request):
        try:
            userToken = request.data.get('userToken')
            print(f"getNickname() -> userToken: {userToken}")
            accountId = self.redisService.getValueByKey(userToken)
            profile = self.accountService.getNickname(accountId)

            if profile is not None:
                nickname = profile.nickname
                return Response({ 'nickname': nickname }, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("사용자 닉네임 가져오는 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def checkAdmin(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            isAdmin = self.accountService.checkAdmin(email, password)
            return Response({ 'isAdmin': isAdmin }, status=status.HTTP_200_OK)

        except Exception as e:
            print('어드민으로 로그인 요청 중 에러 발생:', e)
            return Response(status=status.HTTP_400_BAD_REQUEST)