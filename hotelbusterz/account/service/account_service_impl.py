import os

from account.repository.account_repository_impl import AccountRepositoryImpl
from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service import AccountService

class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def checkEmailDuplication(self, email):
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None

    def checkNicknameDuplication(self, nickname):
        profile = self.__profileRepository.findByNickname(nickname)
        return profile is not None

    def registerAccount(self, loginType, roleType, nickname, email):
        account = self.__accountRepository.create(loginType, roleType)
        return self.__profileRepository.create(nickname, email, account)

    def findAccountByEmail(self, email):
        return self.__profileRepository.findByEmail(email)

    def registerLog(self, accountId, action, actionTime):
        log = self.__accountRepository.createLog(accountId, action, actionTime)
        return log is not None

    def getNickname(self, accountId):
        account = self.__accountRepository.findById(accountId)
        return self.__profileRepository.findByAccount(account)

    def checkAdmin(self, email, password):
        from dotenv import load_dotenv

        load_dotenv()

        ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
        ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
        return email == ADMIN_EMAIL and password == ADMIN_PASSWORD
