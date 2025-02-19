# Функция, которая будет принимать на вход путь к файлу и возвращать сгруппированные данные по городам, 
# содержащие суммарный бюджет и количество кликов.

import numpy as np
import pandas as pd


def group_campaign_data(file_path):
    df = pd.read_csv('campaign_data.csv', encoding='utf-8')
    grouped_campaign = df.groupby('Город', as_index=False).agg({
        'Бюджет': 'sum',
        'Клики': 'sum'
    })

    result_list = []
    for i, row in grouped_campaign.iterrows():
        dct = {'Город': row['Город'], 'Количество кликов': row['Клики'], 'Суммарный бюджет': row['Бюджет']}
        result_list.append(dct)

    return sorted(result_list, key=lambda x: x.keys())


group_campaign_data('campaign_data.csv')
