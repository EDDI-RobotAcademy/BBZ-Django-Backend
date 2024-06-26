from django.db import models

from account.entity.account import Account


class Profile(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    nickname = models.CharField(max_length=64, unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'