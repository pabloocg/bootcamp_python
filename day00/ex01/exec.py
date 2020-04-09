#You will have to make a program that reverses 
# the order of a string and the case of its words.
#If we have more than one argument we have to merge
#  them into a single string and sperate each arg by a ' ' (space char).

#iterable[inicio:fin:paso]

import sys

def reverse(x):
    return x [::-1]

def convert(char):
    if char.islower():
        return char.upper()
    else:
        return char.lower()

def main():
    res = ""
    for i in range(len(sys.argv) - 1, 0, -1):
        res += "".join(convert(char) for char in reverse(sys.argv[i]))
        res += " " if i > 1 else "\n"
    print(res, end='')

if __name__ == "__main__":
    main()