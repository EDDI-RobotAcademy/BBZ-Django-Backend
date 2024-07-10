from django.db import models

from account.entity.account import Account


# Create your models here.
class Marketing(models.Model):
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    acquisition = models.PositiveIntegerField(null=False)
    activation = models.PositiveIntegerField(null=False)
    revenue = models.PositiveIntegerField(null=False)
    retention = models.PositiveIntegerField(null=False)
    referral = models.PositiveIntegerField(null=False)


    def __str__(self):
        return f"marketing -> account:{self.account}, acquisition:{self.acquisition}, activation:{self.activation}, revenue:{self.revenue}, retention:{self.retention}, referral:{self.referral}"

    class Meta:
        db_table = 'marketing'