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

    def register(self, favoritesData, favorites, product):
        FavoritesItem.objects.create(
            favorites=favorites,
            product=product
        )

    def findByFavorites(self, favorites):
        return list(FavoritesItem.objects.filter(favorites=favorites))

    def removeFavoritesItem(self, favorites, product):
        favoritesItem = FavoritesItem.objects.get(favorites=favorites, product=product)
        favoritesItem.delete()


