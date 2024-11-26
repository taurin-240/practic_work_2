# https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset
# Датасет нужно скачать по ссыле и скопировать в директорию этого задания с именем "realtor-data.csv"

import pandas as pd
import msgpack
import kagglehub
import os

# Рабочая директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Загрузим файл
df = pd.read_csv(f"{BASE_DIR}/realtor-data.csv", sep = ",")
print(df.head(6))
print(f"Столбцы: {df.columns}")

#Выберем 7 колонок для анализа данных
df_selected = df[['street', 'city', 'state', 'price', 'bed', 'bath', 'acre_lot']]
print(df_selected.head(6))


df_price = df_selected.iloc[:, 3]
df_bed = df_selected.iloc[:, 4]
df_bath = df_selected.iloc[:, 5]
df_acre_lot = df_selected.iloc[:, 6]
df_city = df_selected.iloc[:, 1]
df_state = df_selected.iloc[:, 2]

city_frequencies = df_city.value_counts().to_dict()
state_frequencies = df_state.value_counts().to_dict()

analysis_results = {'price':
        {'max_price': df_price.max(),
        'min_price': df_price.min(),
        'mean_price': df_price.mean(),
        'sum_price': df_price.sum(),
        'std_price': df_price.std()
         },
'bed':
        {'max_bed': df_bed.max(),
        'min_bed': df_bed.min(),
        'mean_bed': df_bed.mean(),
        'sum_bed': df_bed.sum(),
        'std_bed': df_bed.std()
         },
'bath':
        {'max_bath': df_bath.max(),
        'min_bath': df_bath.min(),
        'mean_bath': df_bath.mean(),
        'sum_bath': df_bath.sum(),
        'std_bath': df_bath.std()
         },
'acre_lot':
        {'max_acre_lot': df_acre_lot.max(),
        'min_acre_lot': df_acre_lot.min(),
        'mean_acre_lot': df_acre_lot.mean(),
        'sum_acre_lot': df_acre_lot.sum(),
        'std_acre_lot': df_acre_lot.std()
         },
'city': city_frequencies,
'state': state_frequencies
}

df.to_pickle(f"{BASE_DIR}/realtor-data.pickle")
df.to_json(f'{BASE_DIR}/realtor-data.json')
with open(f"{BASE_DIR}/realtor-data.msgpack", "wb") as outfile:
    packed = msgpack.packb(df.to_dict())
    outfile.write(packed)

print(f"csv        = {os.path.getsize(f'{BASE_DIR}/realtor-data.csv')}")
print(f"json       = {os.path.getsize(f'{BASE_DIR}/realtor-data.json')}")
print(f"msgpack    = {os.path.getsize(f'{BASE_DIR}/realtor-data.msgpack')}")
print(f"pickle     = {os.path.getsize(f'{BASE_DIR}/realtor-data.pickle')}")


