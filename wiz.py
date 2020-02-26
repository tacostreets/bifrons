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
    def __init__(self, location="tower", skill=0, gold=0, library=2):
        self.location = location
        self.valid_locations = ["tower", "village", "forest"]
        self.skill = skill
        self.gold = gold
        self.library = library

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



    def status(self):
        print(f"You are at the {self.location}.")
        print(f"Your library is level {self.library}.")
        print(f"Your skill level is {self.skill}.")
        print(f"Your purse has {coins(self.gold)}.")


def request(wiz, task):
    if task in wiz.valid_locations:
        wiz.travel(task)
    elif task == "study":
        wiz.study()


            #     -> task is tower
            #         travel to tower
            #     e-> task is study
            #         -> location is tower AND library is sufficient
            #             increase skill
            #         e-> location is not tower
            #             complain about location
            #         e-> library is insufficient
            #             complain about library

            #     e-> task is village
            #         travel to village
            #     e-> task is shop
            #         -> location is village AND gold is sufficient
            #                 increase library AND decrease gold
            #         e-> location is not village
            #             complain about location
            #         e-> gold is zero
            #             you are broke
            #         e-> gold is insufficient
            #             conplain about gold
            #     e-> task is work
            #         -> location is village and skill is sufficient
            #             increase gold
            #         e-> location is not village
            #             complain about location
            #         e-> skill is not sufficient
            #              complain about skill

    elif task == "shop":
        wiz.shop()
    elif task == "work":
        wiz.work()
    elif task == "status":
        wiz.status()

    elif task == "help":
        print("You can do any of the following:")
        print("  help")
        print("  status")
        print("  tower")
        print("    study")
        print("  village")
        print("    shop")
        print("    work")
        print("  forest")
        print("  quit")

    elif task == "quit":
        print("I am now quitting")
        raise EOFError
    else:
        print(f"I don't understand:{task}")


def coins(num):
    if num == 1:
        return f"{num} gold coin"
    else:
        return f"{num} gold coins"


def power(num, P):
    """raises NUM to the exponent P."""
    return num**P


def completion(text, state):
    options = [
        "tower",
        "village",
        "study",
        "work",
        "shop",
        "help",
        "status",
        "quit",
        "forest",
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
