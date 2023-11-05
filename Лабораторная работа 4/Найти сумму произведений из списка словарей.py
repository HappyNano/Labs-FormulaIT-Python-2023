# TODO решите задачу
import json


def task() -> float:
    json_data = {}

    with open("input.json", "r") as fin:
        json_data = json.load(fin)

    return round(sum(list(map(lambda x: x["score"] * x["weight"], json_data))), 3)

print(task())
