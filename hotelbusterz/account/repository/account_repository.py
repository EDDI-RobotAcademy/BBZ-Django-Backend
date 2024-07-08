from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create(self, loginType, roleType):
        pass

    @abstractmethod
    def findById(self, accountId):
        pass

    @abstractmethod
    def createLog(self, accountId, action, actionTime):
        pass


    @abstractmethod
    def createLogDataFrame(self):
        pass

    @abstractmethod
    def accountList(self):
        pass