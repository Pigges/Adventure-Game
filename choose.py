from color import color


def choose(opts: list):

    opts_print = ""

    for i in opts:
        opts_print += "\t" + color('green', i) + "\t"

    size = len(opts_print)
    print(color('red', "-" * size))
    print("\t" + opts_print)
    print(color('red', "-" * size))
