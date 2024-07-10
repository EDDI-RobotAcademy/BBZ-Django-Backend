import random

from django.db import transaction

from account.entity.account import Account
from account.entity.profile import Profile
from orders.entity.orders import Orders
from orders.entity.orders_item import OrdersItem
from orders.entity.orders_status import OrderStatus
from product.entity.models import Product

products = list(Product.objects.all())
account_ids = list(Account.objects.values_list('id', flat=True))


def create_account(login_type_id, role_type_id, nickname, email):
    unique_nickname = nickname
    count = 1
    while Profile.objects.filter(nickname=unique_nickname).exists():
        unique_nickname = f"{nickname}_{count}"
        count +=1

    account = Account.objects.create(loginType_id=login_type_id, roleType_id=role_type_id)
    Profile.objects.create(id=account.id, nickname=unique_nickname, email=email, account_id=account.id)
    return account.id


def create_random_order(account_id):
    try:
        with transaction.atomic():
            order = Orders.objects.create(account_id=account_id, status=OrderStatus.PENDING)

            product = random.choice(products)

            OrdersItem.objects.create(
                orders_id=order.id,
                product_id=product.productId,
            )

    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")


if len(account_ids) < 1000:
    for i in range(len(account_ids), 1000):
        nickname = f"User{i + 1}"
        email = f"user{i + 1}@example.com"
        account_id = create_account(1, 1, nickname, email)
        account_ids.append(account_id)

for _ in range(100000):
    account_id = random.choice(account_ids)
    create_random_order(account_id)

print("Sample data generation completed.")
