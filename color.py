# Color class based from: https://www.geeksforgeeks.org/print-colors-python-terminal/
class Colors:
    def __init__(self):
        self.style = {
            "reset": "\033[0m",
            "bold": "\033[01m",
            "disable": "\033[02m",
            "underline": "\033[04m",
            "reverse": "\033[07m",
            "strikethrough": "\033[09m",
            "invisible": "\033[08m"
        }

        self.fg = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "orange": "\033[33m",
            "blue": "\033[34m",
            "purple": "\033[35m",
            "cyan": "\033[36m",
            "lightgrey": "\033[37m",
            "darkgrey": "\033[90m",
            "lightred": "\033[91m",
            "lightgreen": "\033[92m",
            "yellow": "\033[93m",
            "lightblue": "\033[94m",
            "pink": "\033[95m",
            "lightcyan": "\033[96m"
        }

        self.bg = {
            "black": "\033[40m",
            "red": "\033[41m",
            "green": "\033[42m",
            "orange": "\033[43m",
            "blue": "\033[44m",
            "purple": "\033[45m",
            "cyan": "\033[46m",
            "lightgrey": "\033[47m"
        }


colors = Colors()


def color(c, text, opt=[]):
    """

    :param c: color
    :param text: text
    :param opt: options:
    ['reset', 'bold', 'disable', 'underline', 'reverse', 'strikethrough', 'invisible']
    :return: text with applied color (and options)
    """
    attr = ""

    if opt:
        if 'bg' in opt:
            if c in colors.bg:
                attr += colors.bg[c]
            opt = [o for o in opt if o != 'bg']  # Remove 'bg' from list
        else:
            attr += colors.fg[c]
    else:
        if c in colors.fg:
            attr += colors.fg[c]

    for i in opt:
        if i in colors.style:
            attr += colors.style[i]

    return f"{attr}{text}\033[00m"
