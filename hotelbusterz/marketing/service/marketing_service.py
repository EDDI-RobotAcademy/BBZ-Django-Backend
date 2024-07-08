from abc import ABC, abstractmethod


class MarketingService(ABC):
    @abstractmethod
    def createMarketingData(self):
        pass