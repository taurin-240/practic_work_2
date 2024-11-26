import pickle
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(f"{BASE_DIR}/fourth_task_products.json", "rb") as f:
    products = pickle.load(f)

with open(f"{BASE_DIR}/fourth_task_updates.json", "r", encoding="utf-8") as f:
    updates = json.load(f)

product_map = {}

for product in products:
    product_map[product['name']] = product

for update in updates:
    product = product_map[update['name']]

methods = {
    'percent-': lambda price, param: price * (1 - param),
    'percent+': lambda price, param: price * (1 + param),
    'sub': lambda price, param: price - param,
    'add': lambda price, param: price + param,
}

for update in updates:
    product = product_map[update['name']]
    product['price'] = methods[update['method']](product['price'], update['param'])

products = list(product_map.values())
with open(f"{BASE_DIR}/fourth_task.pkl", "wb") as f:
    pickle.dump(products, f)

