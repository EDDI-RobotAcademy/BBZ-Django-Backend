import os
import django
import random
from django.db import transaction

from product.entity.models import Product
from survey.entity.models import Survey

productList = Product.objects.all()

def create_random_reservation(product_id, lenOfReservation, numOfAdult, numOfChild):
    try:
        with transaction.atomic():
            len_of_reservation = random.randint(lenOfReservation - 5, lenOfReservation)
            num_of_adult = random.randint(1, numOfAdult)
            num_of_child = random.randint(0, numOfChild)
            have_breakfast = random.randint(0, num_of_child + num_of_adult)
            is_exist_car = random.choice([0, 1])

            Survey.objects.create(
                product_id=product_id,
                num_of_adult=num_of_adult,
                num_of_child=num_of_child,
                have_breakfast=have_breakfast,
                is_exist_car=is_exist_car,
                len_of_reservation=len_of_reservation,
            )

    except Exception as e:
        print(f"Error occured in creating dummy database:{e}")


lenOfReservation = 6
numOfAdult = 2
for product in productList:
    i = product.productId
    for _ in range(20000):
        if i == 1 or i == 2 or i == 4:
            numOfChild = 2
        elif i == 3:
            numOfChild = 3
        else:
            numOfChild = 0

        create_random_reservation(i, lenOfReservation, numOfAdult, numOfChild)
    lenOfReservation += 2
    numOfAdult += 1

print("Dummy Data creation Completed.")
