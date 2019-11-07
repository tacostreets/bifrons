#!/usr/bin/env python3

import sys


def main():  # colon marks the beginning of a block of code
    print("You rock!")

    for item in sys.argv:  # talk about for loop 
        print(item)
        
if __name__ == '__main__':
    main()
