#!/usr/bin/env python3 
# shebang Python sees a comment and ignores it 
# Bash (bourne again shell) sees a command to run python3 - telling bash to use python3 
import os.path #importing a top level module(library) 'os' and a sub module 'path' - so it's available to use
from configparser import ConfigParser # from the module 'configparser' import only 'ConfigParser'- a class for a specific kind of config file


def main(): #define a thing 'main()' aka js function
    set_readline() # calling the readline function below
    wiz = load("wiz.save")
    print("Enter your command")
    while True:
        exit_codes = [EOFError, KeyboardInterrupt]
        try:
            task = input("> ") # built-in function and excepts keyboard input back as a string and assigns to task
            result = request(wiz, task) # request defined below as a function
            print(result)
            save(wiz)

        except exit_codes: #exception clause catches an error and executes the next two lines
            print("\nEnd of line user")
            break

def save(wiz):
    data = ConfigParser()
    data["wizard"] = {
        "location": wiz.location,
        "skill": wiz.skill,
        "gold": wiz.gold,
        "library": wiz.library,
        "ingredients": wiz.ingredients,
        "potions": wiz.potions,
    }
    savefile = open("wiz.save", "w")
    data.write(savefile)

def load(filename): # load the variable 'filename' passed thru load() above on line 10
    data = ConfigParser() # CP acts like a dictionary with dictionaries inside of it aka nested dictionaries
    if os.path.isfile(filename): # in os.path is 'filename' a file -isfile is boolean
        data.read(filename) # if yes then read the file
    else:
        data["wizard"] = {} # sets a key to an empty set of dictionaries
    wiz = Wizard(**data["wizard"]) # using the ** method to turn the dictionary into a set of params
    return wiz
        
class Wizard:
    def __init__(self, location="tower", skill=0, gold=0, library=2,ingredients=0, potions=0):
        self.location = location
        self.valid_locations = ["tower", "village", "forest"]
        self.skill = int(skill)
        self.gold = int(gold)
        self.library = int(library)
        self.ingredients = int(ingredients)
        self.potions = int(potions)

    def travel(self, location):
        if self.location == location:
            msg = (f"You are already in the {location}, silly wizard!")
        elif location == "tower":
            msg = ("You travel to your modest one story wizard tower!")
            self.location = "tower"
        elif location == "village":
            msg = ("You travel to the village 100 yds upwind from your tower.")
            self.location = "village"
        elif location == "forest":
            msg = ("You head out into the forest behind your tower.")
            self.location = "forest"
        else:
            msg = (f"I don't know where {location} is.")
        return msg

    def study(self):
        if self.location == "tower" and self.library > self.skill:
            self.skill = self.skill + 1
            msg = f"What a good student! Current skill level is {self.skill}."
        elif self.location != "tower":
            msg = "You can only study in the tower."
        elif self.library <= self.skill:
            msg = f"Your library is {self.library} and your skill level is {self.skill}\n"
            msg = msg + "If you want to improve your skill you need a better library."
        return msg

    def shop(self):
        if self.location == "village" and self.gold >= self.library:
            self.gold = self.gold - self.library
            self.library = self.library + 1
            msg = f"What a good consumer! Library level is {self.library}.\n"
            msg += f"You have {coins(self.gold)} left."
        elif self.location != "village":
            msg = "You can only shop in the village."
        elif self.gold == 0:
            msg =  "Your wallet is empty. You broke."
        elif self.gold < self.library:
            msg = f"You have {coins(self.gold)}. To improve your library, it will cost {coins(self.library)}."
        return msg

    def work(self):
        if self.location == "village" and self.skill > 0:
            self.gold = self.gold + self.skill       #you must have skill to earn gold
            msg = "You provide magical services to the village. They even pay you!\n"
            msg += f"You now have {coins(self.gold)}."
        elif self.location != "village":
            msg = "You can only work in the village"
        elif self.skill <= 0:
            msg = "You don't have enough skill to work. Read a book!"
        return msg

    def gather(self):
        if self.location == "forest":
            self.ingredients = self.ingredients + 1
            msg = "You gather herbs for your potions.\n"
            msg += f"You now have {ingredients(self.ingredients)}."
        else:
            msg = "You can only gather in the forest."
        return msg

    def brew(self):
        if self.location == "tower" and self.ingredients > 0 and self.skill > 0:
            self.potions = self.potions + 1
            self.ingredients = self.ingredients - 1
            msg = f"What a crafty wizard! You now have {potions(self.potions)}.\n"
            msg += f"You have {ingredients(self.ingredients)} left"
        elif self.location != "tower":
            msg = "You can only brew in the tower"
        elif self.skill == 0:
            msg = "You need some skill to brew, go study."
        elif self.ingredients == 0:
            msg = "You can't make a potion without ingredients!"
        return msg

    def sell(self):
        if self.location == "village" and self.potions > 0:
            self.potions = self.potions - 1
            self.gold = self.gold + self.skill * 2
            msg = f"You have sold 1 potion.\n"
            msg += f"You have {potions(self.potions)} potion left.\n"
            msg += f"You now have {coins(self.gold)}."
        elif self.location != "village":
            msg = "You can only sell your potions in the village."
        elif self.potions == 0:
            msg = "You have no potions to sell!"
        return msg



    def status(self):
        msg = f"You are at the {self.location}.\n"
        msg += f"Your library is level {self.library}.\n"
        msg += f"Your skill level is {self.skill}.\n"
        msg += f"Your purse has {coins(self.gold)}.\n"
        msg += f"You have {ingredients(self.ingredients)}.\n"
        msg += f"You have {potions(self.potions)}."
        return msg


def request(wiz, task):
    if task in wiz.valid_locations:
        return wiz.travel(task)
    elif task == "study":
        return wiz.study()
    elif task == "shop":
        return wiz.shop()
    elif task == "work":
        return wiz.work()
    elif task == "status":
        return wiz.status()
    elif task == "gather":
        return wiz.gather()
    elif task == "brew":
        return wiz.brew()
    elif task == "sell":
        return wiz.sell()

    elif task == "help":
        msg = "You can do any of the following:\n"
        msg += "  help\n"
        msg += "  status\n"
        msg += "  tower\n"
        msg += "    study\n"
        msg += "    brew\n"
        msg += "  village\n"
        msg += "    shop\n"
        msg += "    work\n"
        msg += "    sell\n"
        msg += "  forest\n"
        msg += "    gather\n"
        msg += "  quit"
        return msg

    elif task == "quit":
        print("I am now quitting")
        raise EOFError
    else:
        return f"I don't understand:{task}"

def pluralize(noun, num):
    if num == 1:
        return(f"{num} {noun}")
    else:
        return(f"{num} {noun}s")

def coins(num):
    return pluralize("coin", num)

def ingredients(num):
    return pluralize("ingredient", num)

def potions(num):
    return pluralize("potion", num)

def power(num, P):
    """raises NUM to the exponent P."""
    return num**P

def set_readline(): # a set of functions from the readline to complete command line text
    import readline
    readline.set_auto_history(True)
    readline.set_completer(completion)

    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

def completion(text, state):
    options = [
        "tower",
        "brew",
        "study",
        "village",
        "work",
        "shop",
        "help",
        "status",
        "quit",
        "forest",
        "gather",

    ]
    match = []
    for option in options:
        if option.startswith(text):
            match.append(option)
    if state >= len(match):
        return None
    else:
        return match[state]


if __name__=="__main__":
    main()
