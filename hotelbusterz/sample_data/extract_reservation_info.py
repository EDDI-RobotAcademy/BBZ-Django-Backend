import pandas as pd

from survey.entity.models import Survey


def export_reservation_to_excel(file_path):
    # select_related() 관련함수가 뭘 반환해주는지 확인 후 조정 필요
    surveyItems = Survey.objects.select_related('product').all()
    data = []
    for surveyItem in surveyItems:
        data.append({
            'product_id': surveyItem.product_id,
            'len_of_reservation': surveyItem.len_of_reservation,
            'num_of_adult': surveyItem.num_of_adult,
            'num_of_child': surveyItem.num_of_child,
            'have_breakfast': surveyItem.have_breakfast,
            'is_exist_car': surveyItem.is_exist_car,
        })

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Exported reservation data to {file_path}")


file_path = "survey_info.xlsx"
export_reservation_to_excel(file_path)
