from orders.entity.orders_item import OrdersItem
from orders.repository.orders_item_repository import OrdersItemRepository
from product.entity.models import Product


class OrdersItemRepositoryImpl(OrdersItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, orders, product):
        ordersItem = OrdersItem(orders=orders, product=product)
        ordersItem.save()

        return ordersItem

    def findByOrders(self, orders):
        return OrdersItem.objects.get(orders=orders)