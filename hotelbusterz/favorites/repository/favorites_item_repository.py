from abc import ABC, abstractmethod


class FavoritesItemRepository(ABC):
    @abstractmethod
    def findAllByProductId(self, productId):
        pass

    @abstractmethod
    def register(self, favoritesData, favorites, product):
        pass

    @abstractmethod
    def findByFavorites(self, favorites):
        pass

    @abstractmethod
    def removeFavoritesItem(self, favorites, product):
        pass