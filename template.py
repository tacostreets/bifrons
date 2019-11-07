#!/usr/bin/env python3

import sys


def main():  # colon marks the beginning of a block of code
    for name in sys.argv[1:]: # colon in [] is a 'slice' meaning 1 plus the rest of the list   
        print(f"You rock, {name}!")  # f makes this an f-string a formatted string
      
if __name__ == '__main__':
    main()
