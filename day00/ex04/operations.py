import sys

def args_error(n):
    if n > 1 and n < 3:
        print ("InputError: few arguments\n")
    elif n > 3:
        print ("InputError: too many arguments\n")
    usage()

def input_error():
    print ("InputError: only numbers\n")
    usage()

def usage():
    print ("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
    sys.exit(1)

def operations(n1, n2):
    print ("Sum:         " + str(n1 + n2))
    print ("Difference: " + str(n1 - n2))
    print ("Product:     " + str(n1 * n2))
    try:
        print ("Quotient:    " + str(n1 / n2))
    except ZeroDivisionError:
        print ("Quotient:    ERROR (div by zero)")
    try:
        print ("Remainder: " + str(n1 % n2))
    except ZeroDivisionError:
        print ("Remainder: ERROR (modulo by zero)")

def main(argc, argv):
    if argc != 3:
        args_error(argc)
    try:
        number1 = sys.argv[1]
        number1 = int(number1)
        number2 = sys.argv[2]
        number2 = int(number2)
    except ValueError:
        input_error()
    else:
        operations(number1, number2)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)