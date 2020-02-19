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
        self.skill = skill
        self.gold = gold
        self.library = library
    def status(self):
        print(f"You are at the {self.location}.")
        print(f"Your library is level {self.library}.")
        print(f"Your skill level is {self.skill}.")
        print(f"Your purse has {coins(self.gold)}.")


def request(wiz, task):
    if wiz.location == task:
        print(f"You are already in the {task}, silly wizard!")

    elif task == "tower":
        print("You travel to your modest one story wizard tower!")
        wiz.location = "tower"
    elif task == "study":
        if wiz.location == "tower" and wiz.library > wiz.skill:
            wiz.skill = wiz.skill + 1
            print(f"What a good student! Current skill level is {wiz.skill}.")
        elif wiz.location != "tower":
            print("You can only study in the tower.")
        elif wiz.library <= wiz.skill:
            print(f"Your library is {wiz.library} and your skill level is {wiz.skill}")
            print("If you want to improve your skill you need a better library.")

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

    elif task == "village":
        print("You travel to the village 100 yds upwind from your tower.")
        wiz.location = "village"
    elif task == "shop":
        if wiz.location == "village" and wiz.gold >= wiz.library:
            wiz.gold = wiz.gold - wiz.library
            wiz.library = wiz.library + 1
            print(f"What a good consumer! Library level is {wiz.library}.")
            print(f"You have {coins(wiz.gold)} left.")
        elif wiz.location != "village":
            print("You can only shop in the village.")
        elif wiz.gold == 0:
            print ("Your wallet is empty. You broke.")
        elif wiz.gold < wiz.library:
            print(f"You have {coins(wiz.gold)}. To improve your library, it will cost {coins(wiz.library)}.")
    elif task == "work":
        if wiz.location == "village" and wiz.skill > 0:
            wiz.gold = wiz.gold + wiz.skill       #you must have skill to earn gold
            print("You provide magical services to the village. They even pay you!")
            print(f"You now have {coins(wiz.gold)}.")
        elif wiz.location != "village":
            print("You can only work in the village")
        elif wiz.skill <= 0:
            print("You don't have enough skill to work. Read a book!")

    elif task == "forest":
        print("You head out into the forest behind your tower.")
        wiz.location = "forest"

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
    