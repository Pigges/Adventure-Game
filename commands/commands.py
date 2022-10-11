import sys


def show(attr, inventory):
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
    "help": help_command,
    "exit": stop_game
}

sys.modules[__name__] = commands
