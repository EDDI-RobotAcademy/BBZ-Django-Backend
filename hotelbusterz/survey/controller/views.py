from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.entity.models import Survey
from survey.service.survey_service_impl import SurveyServiceImpl


# Create your views here.
class SurveyView(viewsets.ViewSet):
    queryset = Survey.objects.all()
    surveyService = SurveyServiceImpl.getInstance()

    def register(self, request):
        try:
            data = request.data

            productId = data.get('productId')
            numOfAdult = data.get('numOfAdult')
            numOfChild = data.get('numOfChild')
            haveBreakfast = data.get('haveBreakfast')
            isExistCar = data.get('isExistCar')
            lenOfReservation = data.get('lenOfReservation')

            isExistCar = 1 if isExistCar else 0
            numOfChild = int(numOfChild)
            numOfAdult = int(numOfAdult)
            haveBreakfast = int(haveBreakfast)
            
            # print(*map(type, [productId, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation]))

            # if not all([productId, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation]):
                # return Response({'error': '모든 내용을 채워주세요!'},
                #                 status=status.HTTP_400_BAD_REQUEST)

            if numOfAdult < 1:
                return Response({'error': '최소 한 명의 성인은 포함되어야 합니다!'},
                                status=status.HTTP_400_BAD_REQUEST)

            if numOfChild < 0:
                return Response({'error': '올바른 인원 수를 입력해주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            if lenOfReservation < 1:
                return Response({'error': '숙박일수는 하루 이상 선택되어야 합니다!'},
                                status=status.HTTP_400_BAD_REQUEST)

            self.surveyService.createSurvey(productId, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print("예약자 정보 등록 중 문제 발생:", e)
            return Response({ 'error': str(e) },
                            status=status.HTTP_400_BAD_REQUEST)