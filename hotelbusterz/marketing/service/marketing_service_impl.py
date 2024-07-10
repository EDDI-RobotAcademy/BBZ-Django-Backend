from account.repository.account_repository_impl import AccountRepositoryImpl
from marketing.repository.marketing_repository_impl import MarketingRepositoryImpl
from marketing.service.marketing_service import MarketingService


class MarketingServiceImpl(MarketingService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__marketingRepository = MarketingRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createMarketingData(self):
        accountList = self.__accountRepository.accountList()
        dataFrame = self.__accountRepository.createLogDataFrame()
        dataFrameFrom6Month = self.__marketingRepository.createDfFromNMonths(dataFrame, 6)
        dataFrameToDict = self.__marketingRepository.createCountActionPerId(dataFrameFrom6Month)

        marketingData = self.__marketingRepository.createAARRR(accountList, dataFrameToDict)

        return marketingData is not None

    def createtotalAARRR(self, marketingData):
        return self.__marketingRepository.calculateTotal(marketingData)