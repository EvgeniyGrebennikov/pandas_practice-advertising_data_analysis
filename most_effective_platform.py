# Поиск самой эффективной платформы по средним значениям конверсий.

# Результат сохранится в переменной most_effective_platform.

import numpy as np
import pandas as pd

df = pd.read_csv('campaign_data.csv', encoding='utf-8')

platforms_avg_conversions = df.groupby('Платформа').agg(avg_conv=('Конверсия', 'mean'))
platforms_avg_conversions.sort_values('avg_conv', ascending=False, inplace=True)

most_effective_platform = platforms_avg_conversions.index[0]

print(most_effective_platform)
