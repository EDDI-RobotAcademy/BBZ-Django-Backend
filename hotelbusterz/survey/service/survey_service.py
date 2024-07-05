from abc import ABC, abstractmethod


class SurveyService(ABC):
    @abstractmethod
    def createSurvey(self, productId, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation):
        pass