#Функция, которая возвращает средний бюджет всех кампаний, запущенных на определенной платформе.

#Функция calculate_average_budget должна принимать путь к файлу и название плафтормы и возвращать число - средний бюджет всех кампаний, 
#запущенных на данной платформе, округленный до двух знаков после запятой.

import numpy as np
import pandas as pd



def calculate_average_budget(file_path, platform):
  df = pd.read_csv('campaign_data.csv', encoding='utf-8')
  return df[df['Платформа'] == platform]['Бюджет'].mean().round(2)

res = calculate_average_budget('campaign_data.csv', 'Google')
print(res)
