from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productLocation, productActivity, productDining, productPrice, productImageName):
        pass

    @abstractmethod
    def findByProductId(self, productId):
        pass