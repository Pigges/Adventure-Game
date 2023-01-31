import sys


def show(attr, story):
    inventory = story.player.inventory
    if len(attr) > 0:
        attr = attr[0]
    else:
        attr = ""
    actions = {
        "inv": inventory
    }
    if attr == 'help':
        keys = list(actions.keys())
        resp = "Show:"
        for key in keys:
            resp += f"\n- {key}"
        print(resp)
    elif attr in actions:
        print(actions[attr].show())
    else:
        print(f"Cannot show '{attr}'\n'show help' for options")


def opener(attr, story):
    # Shortcut for player inventory
    inventory = story.player.inventory
    # If attributes is bigger than 0 just take the first one
    if len(attr) > 0:
        attr = attr[0]
    # Otherwise just set attribute to empty string for ease later
    else:
        attr = ""
    actions = {}
    # Go through the elements of the room currently in and see what can be opened
    for item in story.content:
        print(item['content'].interact)
        if item['name'] == attr and item['content'].interact == True:
            inventory.add_item('tool', item['content'].collect())
            item['content'].interact = False
            break
        else:
            continue
    else:
        print(f"The {attr} can't be opened")



def help_command(*_):
    keys = list(commands.keys())
    resp = "Commands:"
    for key in keys:
        resp += f"\n- {key}"
    print(resp)


def stop_game(*_):
    print("Goodbye!\nHope to see you again soon.")
    exit()


commands = {
    "show": show,
    "open": opener,
    "help": help_command,
    "exit": stop_game
}

sys.modules[__name__] = commands
