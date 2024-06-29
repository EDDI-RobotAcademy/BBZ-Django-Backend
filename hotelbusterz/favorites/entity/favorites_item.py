from django.db import models

from favorites.entity.favorites import Favorites
from product.entity.models import Product


class FavoritesItem(models.Model):
    favoritesItemId = models.AutoField(primary_key=True)
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return (f"FavoritesItem -> id: {self.favoritesItemId}, "
                f"cart: {self.favorites.favoritesId}, "
                f"product: {self.product.productName}")

    class Meta:
        db_table = 'favorites_item'
        app_label = 'favorites'
