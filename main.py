from intro import intro
from start_menu import start
from player import Player
from commands import commands
from table import show_table
from color import color


# inventory = Inventory()
player = Player()
last = ""


def act():
    cmd = input(f"\n{color('yellow', '>>>')} ")
    if cmd.split(' ')[0] in commands:
        attr = cmd.split(' ')
        attr.pop(0)
        commands[cmd.split(' ')[0]](attr, player.inventory)
        return cmd
    else:
        print("Command does not exist!\n" + color('yellow', "'help'") + " for list of commands")
        return None


intro()
start()

while True:
    new_last = act()
    if new_last:
        last = new_last

    player.inventory.save()

    print(last)

