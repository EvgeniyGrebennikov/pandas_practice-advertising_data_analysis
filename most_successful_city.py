# Поиск самого успешного города проведения кампании по средним значениям конверсий.

# Результат сохранится в переменную most_successful_city

import numpy as np
import pandas as pd

df = pd.read_csv('campaign_data.csv', encoding='utf-8')

most_successful_city = df.groupby('Город').agg(avg_conv=('Конверсия', 'mean')).sort_values('avg_conv', ascending=False).index[0]

print(most_successful_city)
