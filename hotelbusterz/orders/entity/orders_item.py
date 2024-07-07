from django.db import models

from orders.entity.orders import Orders
from product.entity.models import Product


class OrdersItem(models.Model):
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Orders, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderItem {self.id} for Order {self.orders.id}"

    class Meta:
        db_table = 'orders_item'
        app_label = 'orders'