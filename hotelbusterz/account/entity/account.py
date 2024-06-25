from django.db import models

from account.entity.account_role_type import AccountRoleType


class Account(models.Model):
    accountId = models.AutoField(primary_key=True)
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account -> id: {self.accountId}, role: {self.roleType}"

    class Meta:
        db_table = 'account'
        app_label = 'account'