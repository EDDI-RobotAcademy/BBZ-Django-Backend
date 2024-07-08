from abc import ABC, abstractmethod


class OrdersItemRepository(ABC):
    @abstractmethod
    def create(self, orders, product):
        pass

    @abstractmethod
    def findByOrders(self, orders):
        pass