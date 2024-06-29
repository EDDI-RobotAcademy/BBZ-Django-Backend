from abc import ABC, abstractmethod


class FavoritesService(ABC):
    @abstractmethod
    def favoritesRegister(self, favoritesData, accountId):
        pass