#!/usr/bin/env python3

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
    if task == "tower":
        print("You travel to your modest one story wizard tower!")
    elif task == "village":
        print("You travel to the village 100 yds upwind from your tower.")
    elif task == "help":
        print("You can do any of the following:")
        print("  help")
        print("  tower")
        print("  village")
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
    