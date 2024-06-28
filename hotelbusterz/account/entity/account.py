from django.db import models

from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType

class Account(models.Model):
    # accountId = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)

    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    def __str__(self):
        # return f"Account -> id: {self.accountId}, role: {self.roleType}"
        return f"Account -> id: {self.id}, loginType: {self.loginType}, roleType: {self.roleType}"

    class Meta:
        db_table = 'account'
        app_label = 'account'
