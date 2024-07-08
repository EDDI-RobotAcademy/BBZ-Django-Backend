import os
import django
import random
from django.db import transaction

from product.entity.models import Product
from survey.entity.models import Survey

# Django settings 모듈 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelbusterz.settings")
django.setup()

# 기존 호텔 목록 들고오기.
hotel_numbers = list(Product.objects.values_list('productId', flat=True))
print(f"hotel_numbers: {hotel_numbers}")
# 호텔 개수는 총 5개로 설정.
# 호텔 개수가 부족하면 더 만들기
if len(hotel_numbers) < 5:
    for i in range(len(hotel_numbers), 5):
        hotel_numbers.append(i)


def create_random_reservation(product_id):
    try:
        with transaction.atomic():
            product = Product.objects.all()
            productindx = product[product_id]
            # TODO: 랜덤한 값 집어넣기 아직 진행 안됨
            if product_id == 0:
                len_of_reservation = random.randint(1, 6)
                num_of_adult = random.randint(1, 2)
                num_of_child = random.randint(0, 2)
                breakfast_info = random.randint(0, num_of_child + num_of_adult)
                with_car_info = 0
            elif productindx == 1:
                len_of_reservation = random.randint(3, 8)
                num_of_adult = random.randint(1, 3)
                num_of_child = random.randint(0, 2)
                breakfast_info = random.randint(0, num_of_child + num_of_adult)
                with_car_info = 1
            elif productindx == 2:
                len_of_reservation = random.randint(5, 10)
                num_of_adult = random.randint(1, 4)
                num_of_child = random.randint(0, 3)
                breakfast_info = random.randint(0, num_of_child + num_of_adult)
                with_car_info = 1
            elif productindx == 3:
                len_of_reservation = random.randint(7, 12)
                num_of_adult = random.randint(1, 5)
                num_of_child = random.randint(0, 1)
                breakfast_info = random.randint(0, num_of_child + num_of_adult)
                with_car_info = 0
            elif productindx == 4:
                len_of_reservation = random.randint(9, 14)
                num_of_adult = random.randint(1, 6)
                num_of_child = random.randint(0, 1)
                breakfast_info = random.randint(0, num_of_child + num_of_adult)
                with_car_info = 1
            # order(reservation) 도메인 접근 필요.
            Survey.objects.create(
                product=productindx,
                num_of_adult=num_of_adult,
                num_of_child=num_of_child,
                have_breakfast=breakfast_info,
                is_exist_car=with_car_info,
                len_of_reservation=len_of_reservation,
            )

    except Exception as e:
        print(f"Error occured in creating dummy database:{e}")

    pass


# 더미데이터 10만개 만들기
for _ in range(100000):
    # 호텔 랜덤 선택
    product_id = random.choice(hotel_numbers)
    # 랜덤하게 지정한 호텔의 예약정보 생성
    create_random_reservation(product_id)
    pass

print("Dummy Data creation Completed.")
