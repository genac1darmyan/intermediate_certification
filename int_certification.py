import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем столбец в one-hot вид вручную с помощью .loc и циклов
for category in data['whoAmI'].unique():
    data[category] = 0

for i in range(len(data)):
    category = data.loc[i, 'whoAmI']
    data.loc[i, category] = 1

data.head()
