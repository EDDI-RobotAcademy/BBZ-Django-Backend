from abc import ABC, abstractmethod


class FavoritesItemRepository(ABC):
    @abstractmethod
    def findAllByProductId(self, productId):
        pass