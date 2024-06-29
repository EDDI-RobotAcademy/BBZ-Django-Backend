from django.db import models

from account.entity.account import Account


class Favorites(models.Model):
    favoritesId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='favorites')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'favorites -> id: {self.favoritesId}, account: {self.account.id}'

    class Meta:
        db_table = 'favorites'
        app_label = 'favorites'
