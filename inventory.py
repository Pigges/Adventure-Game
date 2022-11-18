from item_types import types
from table import show_table
from color import color
import json


def load():
    """
    :info Loads all items from './data/inv.data'
    :return: [object, object] -> items
    """
    items = []
    file = open("./data/inv.data", "r", encoding="utf-8")
    for line in file.readlines():
        line = line.strip('\n')
        item = json.loads(line)
        item_type = item['type']
        item.pop('type')
        items.append(types[item_type](item))

    file.close()
    return items


def save(inv: list):
    file = open("./data/inv.data", "w", encoding="utf-8")
    for item in inv:
        file.writelines(json.dumps(item.__dict__)+"\n")

    file.close()


def table_inv(cont: dict):
    items = []

    for i in range(len(cont)):
        item = cont[i].info()
        item_id = {"id": i + 1}
        item_id.update(item)
        items.append(item_id)

    return show_table(items, "Here's your inventory:")


class Inventory:
    def __init__(self):
        # print("Inventory initialized!")
        self.items = load()

    def add_item(self, item_type, item):
        self.items.append(types[item_type](item))
        print(f"Received: {color('green', item['name'])}")

    def show(self):
        return table_inv(self.items)

    def save(self):
        save(self.items)
