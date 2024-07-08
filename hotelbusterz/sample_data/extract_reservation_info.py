import os

import django
import pandas

from hotelbusterz.reservation.entity.reservations import Reservations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelbusterz.settings")
django.setup()


def export_reservation_to_excel(file_path):
    # select_related() 관련함수가 뭘 반환해주는지 확인 후 조정 필요
    reservation_items = Reservations.objects.select_related('product').all()
    data = []
    for reservation_item in reservation_items:
        product = reservation_item.product
        data.append({
            'product_number': product.productId,
            'len_of_reservation': reservation_item.len_of_reservation,
            'num_of_adult': reservation_item.num_of_adult,
            'num_of_child': reservation_item.num_of_child,
            'breakfast_info': reservation_item.breakfast_info,
            'with_car_info': reservation_item.with_car_info,
        })
    # pip install pandas
    df = pandas.DataFrame(data)

    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Exported reservation data to {file_path}")


file_path = "reservation_info.xlsx"
export_reservation_to_excel(file_path)
