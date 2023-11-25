# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as f:
        dict_ = json.load(f)
    product = 0
    for line in dict_:
            product += line["score"] * line["weight"]
    return round(product, 3)


print(task())
