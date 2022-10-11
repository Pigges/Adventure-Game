from inventory import Inventory
import sys


class Player:
    def __init__(self):
        self.inventory = Inventory()


sys.modules[__name__] = Player
