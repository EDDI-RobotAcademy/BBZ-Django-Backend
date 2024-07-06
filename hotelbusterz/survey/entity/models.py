from django.db import models

from product.entity.models import Product


# Create your models here.
class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    num_of_adult = models.PositiveIntegerField(default=1)
    num_of_child = models.PositiveIntegerField(default=0)
    have_breakfast = models.PositiveIntegerField(default=0)
    is_exist_car = models.PositiveIntegerField(default=0)
    len_of_reservation = models.PositiveIntegerField(default=1)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'survey'