#!/bin/env python3
from sys import argv

def main():
    if len(argv) < 2:
        print("Usage: initials.py name")
        exit(1)
    name = ""
    for arg in argv[1:]: name += " " + arg
    name = name.strip()
    MAX_LEN = 22

    if len(name) <= MAX_LEN:
        return name
    else:
        words = name.split()
        if len(words[0]) + ( (len(words) - 1) * 3 ) <= MAX_LEN:
            output = words[0]
            for word in words[1:]:
                output += " " + word[0].capitalize() + "."
            return output
        elif len(words[0]) <= MAX_LEN:
            return words[0]
        else:
            return words[0][:MAX_LEN]


if __name__ == '__main__':
    print(main())
