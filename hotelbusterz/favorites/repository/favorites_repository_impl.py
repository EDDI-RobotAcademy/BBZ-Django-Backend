from favorites.entity.favorites import Favorites
from favorites.repository.favorites_repository import FavoritesRepository


class FavoritesRepositoryImpl(FavoritesRepository):
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

    def findByAccount(self, account):
        try:
            favorites = Favorites.objects.get(account=account)
            return favorites
        except Favorites.DoesNotExist:
            print(f"Account로 Favorites 찾을 수 없음! {account}")
            return None

    def register(self, account):
        return Favorites.objects.create(account=account)

