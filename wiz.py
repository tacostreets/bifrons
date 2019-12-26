#!/usr/bin/env python3

def main():
    print("Enter your command")
    while True:
        try: 
            task = input("> ")
            if task == "quit":
                print("I am now quitting")
                break
            elif task == "paradox":
                1 / 0
            print(f"you asked me to:{task}")
        except (EOFError, KeyboardInterrupt):
            print("\nEnd of line user")
            break
        except ZeroDivisionError:
            print("\nDividing by zero is bad")
            
def power(num, P):
    """raises NUM to the exponent P."""
    return num**P 

if __name__=="__main__":
    main()
    