import pandas as pd
import random
from datetime import datetime, timedelta

from django.db import transaction

from account.entity.account import Account
from account.entity.account_log import AccountLog


def randomTime(start_datetime):
    return (start_datetime + \
            timedelta(seconds=random.randint(0, int((end_datetime-start_datetime).total_seconds()))))

def formattedTime(random_datetime):
    return random_datetime.strftime('%Y-%m-%d %H:%M:%S')

# id 추출 후 shuffle 진행
account_ids = list(Account.objects.values_list('id', flat=True))
random.shuffle(account_ids)
# 랜덤 action list
action = ['VIEW_HOME', 'VIEW_BOARD_LIST', 'VIEW_PRODUCT_LIST',
          'BUTTON_FAVORITE', 'BUTTON_BOOKNOW']
# 랜덤 시간 설정 (현재 일로 부터 6개월 전 데이터 사용)
start_datetime = datetime(2024, 1, 12, 0, 0, 0)
end_datetime = datetime.now()

result = []

# activation 이탈율 20%로 만들기 위해 account_ids 200번째 부터 시작하는 것으로 설정
for i, account_id in enumerate(account_ids[200:]):
    time_after_action = randomTime(start_datetime)
    AccountLog.objects.create(account=Account.objects.get(id=account_id),
                              action='LOGIN',
                              action_time=formattedTime(time_after_action))
    # result.append(['LOGIN', formattedTime(time_after_action), account_id])

    randomActionType = random.choices(action, k=(random.randint(0,5)))
    for actionType in randomActionType:
      time_after_action = randomTime(time_after_action)
      AccountLog.objects.create(account=Account.objects.get(id=account_id),
                                action=actionType,
                                action_time=formattedTime(time_after_action))
      # result.append([actionType, formattedTime(time_after_action), account_id])

    # 350번 째부터 order action 추가
    if i >= 150:
        time_after_action = randomTime(time_after_action)
        AccountLog.objects.create(account=Account.objects.get(id=account_id),
                                  action='ORDER',
                                  action_time=formattedTime(time_after_action))
        # result.append(['ORDER', formattedTime(time_after_action), account_id])

    # 700번째 부터 order action 재추가
    if i >= 500:
        for _ in range(random.randint(0,3)):
            randomActionType = random.choices(action, k=(random.randint(0,3)))
            for actionType in randomActionType:
                time_after_action = randomTime(time_after_action)
                AccountLog.objects.create(account=Account.objects.get(id=account_id),
                                          action=actionType,
                                          action_time=formattedTime(time_after_action))
                # result.append([actionType, formattedTime(time_after_action), account_id])

            time_after_action = randomTime(time_after_action)
            AccountLog.objects.create(account=Account.objects.get(id=account_id),
                                      action='ORDER',
                                      action_time=formattedTime(time_after_action))
            # result.append(['ORDER', formattedTime(time_after_action), account_id])

    # 900번 째부터 referral action 추가
    if i >= 700:
        time_after_action = randomTime(time_after_action)
        AccountLog.objects.create(account=Account.objects.get(id=account_id),
                                  action='REFERRAL',
                                  action_time=formattedTime(time_after_action))
