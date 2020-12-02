import json


def load_json(filename):
    return json.load(filename)


def get(dict, key):
    return dict[key]