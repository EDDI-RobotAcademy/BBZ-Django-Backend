from abc import ABC, abstractmethod

class AccountService(ABC):
    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def checkNicknameDuplication(self, nickname):
        pass

    @abstractmethod
    def registerAccount(self, loginType, roleType, nickname, email):
        pass

    @abstractmethod
    def findAccountByEmail(self, email):
        pass

    @abstractmethod
    def registerLog(self, userToken, action, actionTime):
        pass

    @abstractmethod
    def getNickname(self, accountId):
        pass

    @abstractmethod
    def checkAdmin(self, email, password):
        pass