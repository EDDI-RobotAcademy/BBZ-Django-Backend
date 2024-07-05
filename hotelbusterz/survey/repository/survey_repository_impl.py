from survey.entity.models import Survey
from survey.repository.survey_repository import SurveyRepository


class SurveyRepositoryImpl(SurveyRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, product, numOfAdult, numOfChild, haveBreakfast, isExistCar, lenOfReservation):
        survey = Survey(
            product=product,
            num_of_adult=numOfAdult,
            num_of_child=numOfChild,
            have_breakfast=haveBreakfast,
            is_exist_car=isExistCar,
            len_of_reservation=lenOfReservation
        )
        survey.save()
        return survey