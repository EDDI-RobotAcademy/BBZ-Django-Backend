import os
import django
import random
from django.db import transaction

from product.entity.models import Product
from reservation.entity.reservations import Reservations

# Django settings 모듈 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manual_proj.settings")
django.setup()

# 기존 호텔 목록 들고오기.
hotel_numbers = list(Product.object.values_list('productId', flat=True))
print(f"hotel_numbers: {hotel_numbers}")
# 호텔 개수는 총 5개로 설정.
# 호텔 개수가 부족하면 더 만들기
if len(hotel_numbers)<5:
    for i in range(len(hotel_numbers), 5):
        hotel_numbers.append(i)


def create_random_reservation(product_id):
    try:
        with transaction.atomic():
            product = Product.objects.create(product_id = product_id)
            # TODO: 랜덤한 값 집어넣기 아직 진행 안됨
            # order(reservation) 도메인 접근 필요.
            reservation = Reservations.objects.create(
                product_number = product,
                len_of_reservation = 0000,
                num_of_adult = 0000,
                num_of_child = 0000,
                breakfast_info = 0000,
                with_car_info = 0000,
            )

    except Exception as e:
        print("Error occured in creating dummy database.")

    pass


# 더미데이터 10만개 만들기
for _ in range(100000):
    # 호텔 랜덤 선택
    product_id = random.choice(hotel_numbers)
    # 랜덤하게 지정한 호텔의 예약정보 생성
    create_random_reservation(product_id)
    pass


print("Dummy Data creationo Completed.")