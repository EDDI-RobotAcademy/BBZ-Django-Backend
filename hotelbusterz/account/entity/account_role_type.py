from django.db import models


class AccountRoleType(models.Model):
    roleType = models.CharField(max_length=64)

    def __str__(self):
        return self.roleType

    class Meta:
        db_table = 'account_role_type'
        app_label = 'account'