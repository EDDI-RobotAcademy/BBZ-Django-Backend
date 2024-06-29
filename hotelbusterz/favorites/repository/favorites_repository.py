from abc import ABC, abstractmethod


class FavoritesRepository(ABC):
    @abstractmethod
    def findByAccount(self, account):
        pass

    @abstractmethod
    def register(self, account):
        pass