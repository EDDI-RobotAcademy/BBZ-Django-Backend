import os.path

from hotelbusterz import settings
from product.entity.models import Product
from product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
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

    def list(self):
        return Product.objects.all()

    def create(self, productName, productLocation, productActivity, productDining, productPrice, productImageName):
        uploadDirectory = os.path.join(settings.BASE_DIR, "../../BBZ-Vue-Frontend/src/assets/images/uploadImages")
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, productImageName.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in productImageName.chunks():
                destination.write(chunk)

        product = Product(
            productName=productName,
            productLocation=productLocation,
            productActivity=productActivity,
            productDining=productDining,
            productPrice=productPrice,
            productImageName=productImageName.name
        )
        product.save()
        return product

    def findByProductId(self, productId):
        try:
            return Product.objects.get(productId=productId)
        except Product.DoesNotExist:
            return None

