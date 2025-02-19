# Генератор, который будет генерировать даты, в которые НЕ запускались кампании.

# Функция get_missing_campaign_dates должна принимать путь к файлу и генерировать построчно даты, отсортированные по возрастанию, 
# в которые не запускались кампании.


import numpy as np
import pandas as pd
from datetime import date, timedelta


def get_missing_campaign_dates(file_path):
    df = pd.read_csv('campaign_data.csv', encoding='utf-8')

    df['Начальная дата'] = pd.to_datetime(df['Начальная дата']).dt.date
    min_date_start, max_date_start = df['Начальная дата'].min(), df['Начальная дата'].max()

    missing_dates = set()
    day_num = min_date_start

    while day_num <= max_date_start:
        if day_num not in df['Начальная дата'].tolist():
            missing_dates.add(day_num)
        day_num += timedelta(days=1)

    yield from missing_dates


missing_dates = get_missing_campaign_dates('campaign_data.csv')
user_answer = []
for date in missing_dates:
    a = date.strftime('%Y-%m-%d')
    user_answer.append(a)

print(user_answer)
