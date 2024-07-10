from abc import ABC, abstractmethod


class MarketingRepository(ABC):
    @abstractmethod
    def createDfFromNMonths(self, dataFrame, month):
        pass

    @abstractmethod
    def createCountActionPerId(self, dataFrame):
        pass

    @abstractmethod
    def createAARRR(self, accountList, dict):
        pass

    @abstractmethod
    def calculateTotal(self, marketingData):
        pass