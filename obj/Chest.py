import sys
from item_types import types

class Chest:
    def __init__(self) -> None:
        self.interact = True
    
    def collect(self):
        return {"name": "Laser-Sword", "action": "use", "damage": 10, "content": "sword"}

sys.modules[__name__] = Chest