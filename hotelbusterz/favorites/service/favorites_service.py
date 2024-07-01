from abc import ABC, abstractmethod


class FavoritesService(ABC):
    @abstractmethod
    def favoritesRegister(self, favoritesData, accountId):
        pass

    @abstractmethod
    def favoritesList(self, accountId):
        pass