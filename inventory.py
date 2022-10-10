from item_types import types
from table import show_table
from color import color


def table_inv(cont):
    items = []

    for i in range(len(cont)):
        item = cont[i].info()
        item_id = {"id": i + 1}
        item_id.update(item)
        items.append(item_id)

    return show_table(items, "Inventory:")


class Inventory:
    def __init__(self):
        # print("Inventory initialized!")
        self.items = []

    def add_item(self, item_type, item):
        self.items.append(types[item_type](item))
        print(f"Received: {color('green', item['name'])}")

    def show(self):
        return table_inv(self.items)
