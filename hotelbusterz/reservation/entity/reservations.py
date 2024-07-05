from django.db import models

from product.entity.models import Product


class Reservations(models.Model):
    pk_id = models.AutoField(primary_key=True)
    product_number = models.ForeignKey(Product, related_name='product_number', on_delete= models.CASCADE)
    len_of_reservation = models.PositiveIntegerField(default=1)
    num_of_adult = models.PositiveIntegerField(default=1)
    num_of_child = models.PositiveIntegerField(default=1)
    breakfast_info = models.IntegerField(default=0)
    with_car_info=models.IntegerField(default=0)

    def __str__(self):
        return f"reservation number {self.pk_id} reserved hotel number {self.product_number}"

    class Meta:
        db_table='reservation_info'
        app_label = 'reservation'