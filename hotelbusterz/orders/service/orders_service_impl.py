from account.repository.account_repository_impl import AccountRepositoryImpl
from favorites.repository.favorites_item_repository_impl import FavoritesItemRepositoryImpl
from orders.entity.orders_status import OrderStatus
from orders.repository.orders_item_repository_impl import OrdersItemRepositoryImpl
from orders.repository.orders_repository_impl import OrdersRepositoryImpl
from orders.service.orders_service import OrdersService
from product.repository.product_repository_impl import ProductRepositoryImpl


class OrdersServiceImpl(OrdersService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__ordersRepository = OrdersRepositoryImpl.getInstance()
            cls.__instance.__ordersItemRepository = OrdersItemRepositoryImpl.getInstance()
            cls.__instance.__favoritesItemRepository =FavoritesItemRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createOrder(self, accountId, productId):
        try:
            orders = self.__ordersRepository.create(accountId, OrderStatus.PENDING)
            product = self.__productRepository.findByProductId(productId)
            self.__ordersItemRepository.create(
                orders,
                product
            )

            return orders.id

        except Exception as e:
            print('Error creating order:', e)
            raise e

    def readOrderDetails(self, ordersId, accountId):
        try:
            orders = self.__ordersRepository.findById(ordersId)

            if orders.account.id != int(accountId):
                raise ValueError('Invalid accountId for this order')

            print("check order object <- readOrderDetails()")

            ordersItem = self.__ordersItemRepository.findByOrders(orders)
            product = self.__productRepository.findByProductId(ordersItem.product_id)

            order_details = {
                'orders': {
                    'id': orders.id,
                    'status': orders.status,
                    'created_date': orders.created_date,
                },
                'orders_items': {
                    'product_id': ordersItem.product_id,
                    'product_name': product.productName,
                    'product_price': product.productPrice,
                }
            }

            return order_details

        except Exception as e:
            print('Error reading order details:', e)
            raise e

    def ordersList(self, accountId):
        account = self.__accountRepository.findById(accountId)
        accountOrder = self.__ordersRepository.findByAccount(account)