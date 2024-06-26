# from django.db import models
#
# from account.entity.account import Account
#
#
# class AccountLog(models.Model):
#     accountId = models.ForeignKey(Account.accountId, on_delete=models.CASCADE)
#     logPoint = models.CharField(max_length=64*2)
#     logTime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Log -> id: {self.accountId}, log: {self.logPoint} | {self.logTime}"
#
#     class Meta:
#         db_table = 'account_log'
#         app_label = 'account'