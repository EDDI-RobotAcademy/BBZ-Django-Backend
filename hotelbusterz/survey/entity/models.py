from django.db import models

from product.entity.models import Product


# Create your models here.
class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    num_of_adult = models.PositiveIntegerField()
    num_of_child = models.PositiveIntegerField()
    have_breakfast = models.PositiveIntegerField()
    is_exist_car = models.PositiveIntegerField()
    len_of_reservation = models.PositiveIntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'survey'