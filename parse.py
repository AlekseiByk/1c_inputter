import pandas as pd
import numpy as np


def ParseTable(filename):
    df = pd.read_excel(filename, sheet_name='Лист1')

    data = dict()

    iterator = 0

    for i in df.index:
        name = '{0} {1} {2}'.format(df['Фамилия'][i], df['Имя'][i], df['Отчество'][i] if not (df['Отчество'][i] != df['Отчество'][i]) else "" )
        sum = int(df['Итоговая \nсумма'][i])
        cat = str(df['Рекомендованные\nкатегории'][i])
        group = str(df['Учебная группа'][i])

        flag = True
        for j in range(iterator):
            if  data[j]['ФИО'] == name:
                data[j]['Сумма']     += sum
                data[j]['Категория'] += cat
                flag = False
                break

        if flag:
            data[iterator] = {
                'ФИО': name,
                'Сумма': sum,
                'Категория': cat,
                'группа': group,
            }
            iterator += 1

    return data

def ParseCategory(raw_data):
    raw_data = raw_data.split('\n')
    data = raw_data

    return data
	