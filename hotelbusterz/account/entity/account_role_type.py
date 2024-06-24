from django.db import models


class AccountRoleType(models.Model):
    class RoleType(models.TextChoices):
        ROLE = 'customer', 'admin'
    roleType = models.CharField(max_length=30, choices=RoleType.choices)

    def __str__(self):
        return f"roleType -> {self.roleType}"

    class Meta:
        db_table = 'account_role_type'
        app_label = 'account'