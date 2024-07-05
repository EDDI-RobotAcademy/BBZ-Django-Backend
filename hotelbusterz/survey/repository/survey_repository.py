from abc import ABC, abstractmethod


class SurveyRepository(ABC):
    @abstractmethod
    def create(self, product, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation):
        pass