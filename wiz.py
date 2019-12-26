#!/usr/bin/env python3

def main():
    print("Enter your command")
    while True:
        try: 
            task = input("> ")
            if task == "quit":
                print("I am now quitting")
                break
            print(f"you asked me to:{task}")
        except:
            print("\nEnd of line user")
            break
            
def power(num, P):
    """raises NUM to the exponent P."""
    return num**P 

if __name__=="__main__":
    main()
    