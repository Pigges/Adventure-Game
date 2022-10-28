from intro import intro
from start_menu import start
from story import Story
from commands import commands
from table import show_table
from color import color

last = ""


def act():
    cmd = input(f"\n{color('yellow', '>>>')} ")
    if cmd.split(' ')[0] in commands:
        attr = cmd.split(' ')
        attr.pop(0)
        commands[cmd.split(' ')[0]](attr, story)
        return cmd
    else:
        print("Command does not exist!\n" + color('yellow', "'help'") + " for list of commands")
        return None


intro()
story = Story()

while True:
    story.play()
    new_last = act()
    if new_last:
        last = new_last

    story.player.inventory.save()

    print(last)

