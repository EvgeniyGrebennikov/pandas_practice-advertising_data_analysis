# Рассчитать долю затрат на рекламные кампании каждой платформы и каждого города.
# Результат сохранится в файле platform_city_results.txt.

# Результат должен иметь такой же порядок групп, что и изначальный файл. А города внутри платформ должны быть отсортированы по 
# убыванию доли затрат, а доля затрат должны быть округлена до 2 знаков после запятой.

import numpy as np
import pandas as pd

df = pd.read_csv('campaign_data.csv', encoding='utf-8')

platform_city_cost = df.groupby(['Платформа', 'Город'], as_index=False).agg(cost=('Бюджет', 'sum'))
platform_city_cost
platform_total_cost = platform_city_cost.groupby('Платформа', as_index=False).agg(total_cost=('cost', 'sum'))
platform_city_results = platform_city_cost.merge(platform_total_cost, how='inner', left_on='Платформа',
                                                 right_on='Платформа')
platform_city_results['share_cost'] = (platform_city_results['cost'] / platform_city_results['total_cost'] * 100).round(2)

platform_city_results = platform_city_results[['Платформа', 'Город', 'share_cost']]

# Выводим уникальные значения названия платформ в исходном порядке
platforms_order = df['Платформа'].drop_duplicates().tolist()

# Меняем тип данных на категориальный
platform_city_results['Платформа'] = pd.Categorical(platform_city_results['Платформа'], categories=platforms_order, ordered=True)

platform_city_results = platform_city_results.sort_values(['Платформа', 'share_cost'], ascending=[True, False])
platform_city_results.reset_index(drop=True, inplace=True)

with open('platform_city_results.txt', 'w', encoding='utf-8') as res_file:
    for platform in platforms_order:
        data = platform_city_results[platform_city_results['Платформа'] == platform]

        print(f'Для группы {platform}:', file=res_file)

        for i, row in data.iterrows():
            print(f"- Город: {row['Город']}, доля затрат на рекламу: {row['share_cost']}%", file=res_file)   
