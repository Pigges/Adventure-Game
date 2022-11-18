from typer import typer
from time import sleep


def intro():
    typer("You are finally here!")
    sleep(0.5)
    typer("I really need your help right now")
    sleep(0.5)
    typer("I just got robbed!")
    typer("Then he ran to the back, but I'm to afraid to look")
    typer("He has a sword...")
    sleep(1)
    print("\n\nYou go to the back...")


