import time


def typer(text):
    for i in text:
        print(i, end='')
        time.sleep(0.05)
    print("")
