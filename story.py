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
        self.robber = True
        self.chest = True
        rand = random.randint(1, 10)
        if rand <= 7:
            self.door = 1
        else:
            self.door = 2
    
    def play(self):
        if self.state == 'start':
            self.start()
        elif self.state == 'chest_room':
            self.chest_room()
        elif self.state == 'rob_room':
            self.rob_room()
        else:
            print("Something that shouldn't be happening just happened. Weird!")

    def start(self):
        """
        Where you start and get the option to choose what door you want to enter
        """

        print("You find two doors,")
        print("Which one do you enter?")
        options = ['Left', 'Right']
        back = False
        for item in self.player.inventory.items:
            if item.type == 'tool':
                back = True
                break
        if back:
            options.append('Back')
        ans = option(options)
        typer("You opened the " + ans[1] + " door")
        if ans[0] == self.door:
            if self.chest:
                typer("and find yourself in a room with a big chest.")
                typer("Open the chest by typing: " + color("yellow", "open chest"))
                self.content = [{"name": "chest", "content": Chest(), "interact": True}]
                self.state = 'chest_room'
                self.chest = False
            else:
                print("\nYou have already been here, going back.\n")
                self.start()
        elif ans[0] == 3 and back:
            typer("You went back to the store...")
        else:
            self.rob_room()

    def chest_room(self):
        if (self.content[0]['name'] == "chest" and self.content[0]['content'].interact == False):
            self.state = 'start'
            self.start()

    def rob_room(self):
        if self.robber:
            for item in self.player.inventory.items:
                if item.type == 'tool':
                    typer("This time you are well prepared and stabs the robber in the chest before they realize it.")
                    self.content = [{"name": "Money", "amount": "$300", "interact": True}]
                    break
            else:
                typer("and the robber stabs you in the chest.\nYou die!")
                typer("Thanks for playing!\nYou are welcome to try again whenever.")
                exit()

        



def option(opts: list):
    while True:
        try:
            choose(opts)
            ans = input("Answer: ").lower()
            if ans == "left":
                return [1, ans]
            elif ans == "right":
                return [2, ans]
            elif ans == "back":
                return [3, ans]
        except:
            print("Invalid input")