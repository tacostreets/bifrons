#!/usr/bin/env python3
import readline

# calling out the variables as globals
WIZ_LOCATION = "tower"
WIZ_SKILL = 0
WIZ_LIBRARY = 3
WIZ_GOLD = 0

def main():
    readline.set_auto_history(True)
    print("Enter your command")
    while True:
        try: 
            task = input("> ")
            request(task)

        except (EOFError, KeyboardInterrupt):
            print("\nEnd of line user")
            break
# using the globals assigned above with "global"
def request(task):
    global WIZ_LOCATION  # tower village forest
    global WIZ_SKILL  # study improves this, library limits this
    global WIZ_LIBRARY  # shop improves this
    global WIZ_GOLD  # work increases this, shop decreases this
    if WIZ_LOCATION == task:
        print(f"You are already in the {task}, silly wizard!")

    elif task == "tower":
        print("You travel to your modest one story wizard tower!")
        WIZ_LOCATION = "tower"
    elif task == "study":
        if WIZ_LOCATION == "tower" and WIZ_LIBRARY > WIZ_SKILL:
            WIZ_SKILL = WIZ_SKILL + 1
            print(f"What a good student! Current skill level is {WIZ_SKILL}.")
        elif WIZ_LOCATION != "tower":
            print("You can onlyn study in the tower.")
        elif WIZ_LIBRARY <= WIZ_SKILL:
            print(f"Your library is {WIZ_LIBRARY} and your skill level is {WIZ_SKILL}")
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
        WIZ_LOCATION = "village"
    elif task == "shop":
        if WIZ_LOCATION == "village" and WIZ_GOLD >= WIZ_LIBRARY:
            WIZ_GOLD = WIZ_GOLD - WIZ_LIBRARY
            WIZ_LIBRARY = WIZ_LIBRARY + 1
            print(f"What a good consumer! Library level is {WIZ_LIBRARY}.")
            print(f"You have {coins(WIZ_GOLD)} left.")
        elif WIZ_LOCATION != "village":
            print("You can only shop in the village.")
        elif WIZ_GOLD == 0:
            print ("Your wallet is empty. You broke.")
        elif WIZ_GOLD < WIZ_LIBRARY:
            print(f"You have {coins(WIZ_GOLD)}. To improve your library, it will cost {coins(WIZ_LIBRARY)}.")
    elif task == "work":
        if WIZ_LOCATION == "village" and WIZ_SKILL > 0:
            WIZ_GOLD = WIZ_GOLD + WIZ_SKILL       #you must have skill to earn gold
            print("You provide magical services to the village. They even pay you!")
            print(f"You now have {coins(WIZ_GOLD)}.")
        elif WIZ_LOCATION != "village":
            print("You can only work in the village")
        elif WIZ_SKILL <= 0:
            print("You don't have enough skill to work. Read a book!")

    elif task == "forest":
        print("You head out into the forest behind your tower.")
        WIZ_LOCATION = "forest"

    elif task == "help":
        print("You can do any of the following:")
        print("  help")
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


if __name__=="__main__":
    main()
    