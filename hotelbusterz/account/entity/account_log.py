from django.db import models

from account.entity.account import Account
from account.entity.action_type import ActionType


class AccountLog(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    action = models.CharField(max_length=64, default=ActionType.VIEW_HOME)
    action_time = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"account_log -> account_id:{self.account_id}, action:{self.action}, time:{self.action_time}"

    class Meta:
        db_table = 'account_log'
        app_label = 'account'
