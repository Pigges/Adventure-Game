from commands import commands
from inventory import Inventory
from table import show_table
from color import color


inventory = Inventory()
last = ""

inventory.add_item("text", {"name": "Letter", "action": "read", "content": "Hello and welcome to this game"})
inventory.add_item("tool", {"name": "Laser-Sword", "action": "use", "damage": 10, "content": "sword"})

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
        # attr = cmd.split(' ')[1]
        # print(actions[attr].show())
        return None


while True:
    new_last = act()
    if new_last:
        last = new_last

    print(last)

