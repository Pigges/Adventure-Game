from choose import choose
from typer import typer
from time import sleep
import random


def intro():
    typer("You are finally here!")
    sleep(0.5)
    typer("I really need your help right now")
    sleep(0.5)
    typer("I just got robbed!")
    typer("Then he ran to the back, but I'm to afraid to look")
    typer("He has a sword...")
    sleep(1)
    print("\n\nYou go to the back and find two doors,")
    print("Which one do you enter?")
    ans = option(['Left', 'Right'])
    rand = random.randint(1, 2)
    if ans[0] == rand:
        print("You survived!")
    else:
        print("You opened the " + ans[1] + " door\nand the robber stabs you in the chest.\nYou die!")


def option(opts: list):
    while True:
        try:
            choose(opts)
            ans = input("Answer: ").lower()
            if ans == "left":
                return [1, ans]
            elif ans == "right":
                return [2, ans]
        except:
            print("Invalid input")
