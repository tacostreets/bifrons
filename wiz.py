#!/usr/bin/env python3

WIZ_LOCATION = "tower"
WIZ_SKILL = 0
WIZ_LIBRARY = 3
WIZ_GOLD = 0

def main():
    print("Enter your command")
    while True:
        try: 
            task = input("> ")
            request(task)

        except (EOFError, KeyboardInterrupt):
            print("\nEnd of line user")
            break

def request(task):
    global WIZ_LOCATION
    global WIZ_SKILL
    global WIZ_LIBRARY
    global WIZ_GOLD
    if WIZ_LOCATION == task:
        print(f"You are already in the {task}, silly wizard!")
    elif task == "tower":
        print("You travel to your modest one story wizard tower!")
        WIZ_LOCATION = "tower"
    elif task == "study":
        if WIZ_LOCATION == "tower" and WIZ_LIBRARY > WIZ_SKILL:
            WIZ_SKILL = WIZ_SKILL + 1
            print(f"What a good student! Current skill level is {WIZ_SKILL}.")
        else:
            if WIZ_LOCATION != "tower":
                print ("You can only study in the tower")
            else:
                print(f"Your library is {WIZ_LIBRARY} and your skill level is {WIZ_SKILL}")
                print("If you want to improve your skill you need a better library.")

    elif task == "village":
        print("You travel to the village 100 yds upwind from your tower.")
        WIZ_LOCATION = "village"
    elif task == "shop":
        if WIZ_LOCATION == "village":
            if WIZ_GOLD >= WIZ_LIBRARY:
                WIZ_LIBRARY = WIZ_LIBRARY + 1
                WIZ_GOLD = WIZ_GOLD - WIZ_LIBRARY
                print(f"What a good consumer! Library level is {WIZ_LIBRARY}.")
                print(f"You have {WIZ_GOLD} gold left.")
            else:
                print("Your wallet is empty. You broke.")
        else:
            print("You can only shop in the village.")
    elif task == "work":
        if WIZ_LOCATION == "village":
            WIZ_GOLD = WIZ_GOLD + WIZ_SKILL       #you must have skill to earn gold
            print("You provide magical services to the village. They even pay you!")
            print(f"You now have {WIZ_GOLD} gold.")
        else:
            print("You can only work in the village.")
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

def power(num, P):
    """raises NUM to the exponent P."""
    return num**P 

if __name__=="__main__":
    main()
    