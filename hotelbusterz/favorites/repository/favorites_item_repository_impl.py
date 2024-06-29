from favorites.entity.favorites_item import FavoritesItem
from favorites.repository.favorites_item_repository import FavoritesItemRepository


class FavoritesItemRepositoryImpl(FavoritesItemRepository):
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

    def findAllByProductId(self, productId):
        return FavoritesItem.objects.filter(product_id=productId)

