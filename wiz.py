#!/usr/bin/env python3
import readline

def main():
    readline.set_auto_history(True)
    readline.set_completer(completion)
    wiz = Wizard()
    print("Enter your command")
    while True:
        try:
            task = input("> ")
            request(wiz, task)

        except (EOFError, KeyboardInterrupt):
            print("\nEnd of line user")
            break


class Wizard:
    def __init__(self, location="tower", skill=0, gold=0, library=2,ingredients=0, potions=0):
        self.location = location
        self.valid_locations = ["tower", "village", "forest"]
        self.skill = skill
        self.gold = gold
        self.library = library
        self.ingredients = ingredients
        self.potions = potions

    def travel(self, location):
        if self.location == location:
            print(f"You are already in the {location}, silly wizard!")
        elif location == "tower":
            print("You travel to your modest one story wizard tower!")
            self.location = "tower"
        elif location == "village":
            print("You travel to the village 100 yds upwind from your tower.")
            self.location = "village"
        elif location == "forest":
            print("You head out into the forest behind your tower.")
            self.location = "forest"
        else:
            print(f"I don't know where {location} is.")

    def study(self):
        if self.location == "tower" and self.library > self.skill:
            self.skill = self.skill + 1
            print(f"What a good student! Current skill level is {self.skill}.")
        elif self.location != "tower":
            print("You can only study in the tower.")
        elif self.library <= self.skill:
            print(f"Your library is {self.library} and your skill level is {self.skill}")
            print("If you want to improve your skill you need a better library.")

    def shop(self):
        if self.location == "village" and self.gold >= self.library:
            self.gold = self.gold - self.library
            self.library = self.library + 1
            print(f"What a good consumer! Library level is {self.library}.")
            print(f"You have {coins(self.gold)} left.")
        elif self.location != "village":
            print("You can only shop in the village.")
        elif self.gold == 0:
            print ("Your wallet is empty. You broke.")
        elif self.gold < self.library:
            print(f"You have {coins(self.gold)}. To improve your library, it will cost {coins(self.library)}.")

    def work(self):
        if self.location == "village" and self.skill > 0:
            self.gold = self.gold + self.skill       #you must have skill to earn gold
            print("You provide magical services to the village. They even pay you!")
            print(f"You now have {coins(self.gold)}.")
        elif self.location != "village":
            print("You can only work in the village")
        elif self.skill <= 0:
            print("You don't have enough skill to work. Read a book!")

    def gather(self):
        if self.location == "forest":
            self.ingredients = self.ingredients + 1
            print("You gather herbs for your potions.")
            print(f"You now have {ingredients(self.ingredients)}.")
        else:
            print("You can only gather in the forest.")

    def brew(self):
        if self.location == "tower" and self.ingredients > 0 and self.skill > 0:
            self.potions = self.potions + 1
            self.ingredients = self.ingredients - 1
            print(f"What a crafty wizard! You now have {potions(self.potions)}.")
            print(f"You have {ingredients(self.ingredients)} left")
        elif self.location != "tower":
            print("You can only brew in the tower")
        elif self.skill == 0:
            print("You need some skill to brew, go study.")
        elif self.ingredients == 0:
            print("You can't make a potion without ingredients!")

    def sell(self):
        if self.location == "village" and self.potions > 0:
            self.potions = self.potions - 1
            self.gold = self.gold + self.skill * 2
            print(f"You have sold 1 potion.")
            print(f"You have {potions(self.potions)} potion left.")
            print(f"You now have {coins(self.gold)}.")
        elif self.location != "village":
            print("You can only sell your potions in the village.")
        elif self.potions == 0:
            print("You have no potions to sell!")



    def status(self):
        print(f"You are at the {self.location}.")
        print(f"Your library is level {self.library}.")
        print(f"Your skill level is {self.skill}.")
        print(f"Your purse has {coins(self.gold)}.")
        print(f"You have {ingredients(self.ingredients)}.")
        print(f"You have {potions(self.potions)}.")


def request(wiz, task):
    if task in wiz.valid_locations:
        wiz.travel(task)
    elif task == "study":
        wiz.study()
    elif task == "shop":
        wiz.shop()
    elif task == "work":
        wiz.work()
    elif task == "status":
        wiz.status()
    elif task == "gather":
        wiz.gather()
    elif task == "brew":
        wiz.brew()
    elif task == "sell":
        wiz.sell()

    elif task == "help":
        print("You can do any of the following:")
        print("  help")
        print("  status")
        print("  tower")
        print("    study")
        print("    brew")
        print("  village")
        print("    shop")
        print("    work")
        print("    sell")
        print("  forest")
        print("    gather")
        print("  quit")

    elif task == "quit":
        print("I am now quitting")
        raise EOFError
    else:
        print(f"I don't understand:{task}")

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
