# Генератор, который будет генерировать данные о кампаниях, запущенных в указанном городе и имеющих бюджет выше заданного значения.

#Функция campaign_generator должна принимать путь к файлу, город и бюджет и генерировать словари,
# отсортированные по возрастанию 'ID Кампании' в формате:

import numpy as np
import pandas as pd


def campaign_generator(file_path,  city, cost):
  df = pd.read_csv('campaign_data.csv', encoding='utf-8')
  df = df[(df['Город'] == city) & (df['Бюджет'] > cost)].sort_values('ID Кампании')

  for i, row in df.iterrows():
    dct = {'ID Кампании': str(row['ID Кампании']), 'Тип': str(row['Тип кампании']), 'Платформа': str(row['Платформа']), 'Доход': str(row['Доход'])}
    yield dct


campaigns = campaign_generator('campaign_data.csv', 'Москва', 48000)
user_answer = []
for campaign in campaigns:
    user_answer.append(campaign)

print(user_answer)
