import os.path as path
import config
import json

stocks_path = path.join(config.root, "data", "stocks.json")


def record(data):
    with open(stocks_path, "w") as writer:
        json.dump(data, writer)


def get():
    with open(stocks_path, "r") as reader:
        data = json.load(reader)

    return data
