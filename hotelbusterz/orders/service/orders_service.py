from abc import ABC, abstractmethod


class OrdersService(ABC):
    @abstractmethod
    def createOrder(self, accountId, productId):
        pass

    @abstractmethod
    def readOrderDetails(self, ordersId, accountId):
        pass

    @abstractmethod
    def ordersList(self, accountId):
        pass