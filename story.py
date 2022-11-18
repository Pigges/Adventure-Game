from choose import choose
from player import Player
from color import color
from typer import typer
from obj import Chest
import random

class Story:
    def __init__(self):
        self.player = Player()
        self.state = 'start'
        self.door = 0
        rand = random.randint(1, 10)
        if rand <= 7:
            self.door = 1
        else:
            #self.door = 2
            self.dor = 1 # remember to change later
    
    def play(self):
        if self.state == 'start':
            self.start()
        if self.state == 'chest_room':
            self.chest_room()
        else:
            print("Something that shouldn't be happening just happened. Weird!")

    def start(self):
        print("You find two doors,")
        print("Which one do you enter?")
        ans = option(['Left', 'Right'])
        typer("You opened the " + ans[1] + " door")
        if ans[0] == self.door:
            self.state = 'chest_room'
            typer("and find yourself in a room with a big chest.")
            typer("Open the chest by typing: " + color("yellow", "open chest"))
            self.content = [{"name": "Chest", "content": Chest(), "interect": True}]
        else:
            typer("and the robber stabs you in the chest.\nYou die!")
            typer("Thanks for playing!\nYou are welcome to try again whenever.")
            exit()

    def chest_room(self):
        pass


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