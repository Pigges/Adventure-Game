from color import color


def get_biggest(cont):
    # Get the biggest string in dict
    biggest = {}
    for i in range(len(cont)):
        for key, val in cont[i].items():
            if key in biggest:
                if len(key) > biggest[key]:
                    biggest[key] = len(key)
            else:
                biggest[key] = len(key)

            if len(str(val)) > biggest[key]:
                biggest[key] = len(str(val))
    return biggest


def show_table(cont, title):
    biggest = get_biggest(cont)

    pipe = color('purple', '|')
    plus = color('purple', '+')

    table = ["", "", ""]
    # Create the head for the table

    # +-----+-----+-----+
    # | Key | Key | Key |
    # +=====+=====+=====+
    for key in biggest:
        table[0] += f"{plus}{color('blue', '-') * (biggest[key] + 2)}"
        table[1] += f"{pipe} {color('yellow', key.capitalize())}{' ' * (biggest[key] - len(key))} "
        table[2] += f"{plus}{color('blue', '=') * (biggest[key] + 2)}"
    table[0] += plus
    table[1] += pipe
    table[2] += plus

    # Add each item to the table

    # | Value | Value | Value |
    # +-------+-------+-------+
    for i in range(len(cont)):
        item = ""
        br = ""
        for key, val in biggest.items():
            if key in cont[i]:
                value = color('green', cont[i][key])
                item += f"{pipe} {value}{' ' * (biggest[key] - len(str(cont[i][key])))} "
            else:
                item += f"{pipe} {color('green', '-')}{' ' * (biggest[key] - 1)} "
            br += f"{plus}{color('blue', '-') * (biggest[key] + 2)}"
        table.append(f"{item}{pipe}")
        table.append(f"{br}{plus}")

    resp = title
    for i in table:
        resp += "\n" + i

    return resp
