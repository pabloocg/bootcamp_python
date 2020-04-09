import sys

def main():
    if len(sys.argv) != 2 or sys.argv[1].isdigit() == False:
        print ("ERROR")
        exit(1)
    number = int(sys.argv[1])
    if number == 0:
        print ("I'm Zero.")
    elif number % 2:
        print ("I'm Odd.")
    else:
        print ("I'm Even.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()