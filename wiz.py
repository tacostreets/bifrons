#!/usr/bin/env python3

def main():
    while True:
        task = input("> ")
        if task == "quit":
            break
        print(f"you asked me to:{task}")
            
def power(num, P):
    """raises NUM to the exponent P."""
    return num**P 

if __name__=="__main__":
    main()