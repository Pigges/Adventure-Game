from commands import commands
from inventory import Inventory
from table import show_table
from color import color
import json


inventory = Inventory()
last = ""

# print(inventory.items[0].save())
# print(inventory.items[1].save())

print(color('orange', 'Hello!', ['bolds']))
print("You do want to do this right? ")

print(show_table([{"Name": "something", "Usage": "IDK"}], "Hello"))


def act():
    cmd = input(f"\n{color('yellow', '>>>')} ")
    if cmd.split(' ')[0] in commands:
        attr = cmd.split(' ')
        attr.pop(0)
        commands[cmd.split(' ')[0]](attr, inventory)
        return cmd
    else:
        print("Command does not exist!\n'help' for list of commands")
        return None


while True:
    new_last = act()
    if new_last:
        last = new_last

    inventory.save()

    print(last)

