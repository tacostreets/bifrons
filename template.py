#!/usr/bin/env python3


def main():  # colon marks the beginning of a block of code
    while True:
        task = input("wat? ")
        if task == "quit":
            break
        print(f"Did {task}")

if __name__ == '__main__': # this calls the script from the command line
    main()
