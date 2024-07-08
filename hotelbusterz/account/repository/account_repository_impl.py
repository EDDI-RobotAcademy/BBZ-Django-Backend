import datetime
import pandas as pd

from account.entity.account import Account
from account.entity.account_log import AccountLog
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
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

    def create(self, loginType, roleType):
        loginTypeEntity, _ = AccountLoginType.objects.get_or_create(loginType=loginType)
        roleTypeEntity, _ = AccountRoleType.objects.get_or_create(roleType=roleType)

        account = Account.objects.create(loginType=loginTypeEntity, roleType=roleTypeEntity)
        return account

    def findById(self, accountId):
        account = Account.objects.get(id=accountId)
        return account

    def changeToFormattedTime(self, time):
        timestamp = int(time) / 1000
        datetime_obj = datetime.datetime.fromtimestamp(timestamp)
        formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime

    def createLog(self, accountId, action, actionTime):
        account = Account.objects.get(id=accountId)
        forttedActionTime = self.changeToFormattedTime(actionTime)
        log = AccountLog.objects.create(account=account, action=action, action_time=forttedActionTime)

        return log


    def createLogDataFrame(self):
        tupleData = AccountLog.objects.values_list("account_id", "action", "action_time")
        dataFrameData = pd.DataFrame(tupleData, columns=["account_id", "action", "action_time"])
        dataFrameData["action_time"] = pd.to_datetime(dataFrameData["action_time"])
        return dataFrameData

    def accountList(self):
        return Account.objects.all()