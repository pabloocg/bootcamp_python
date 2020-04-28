import sys

def error_message():
    sys.exit("ERROR")

def filterInput(stringw, limit):
    words = stringw.split()
    filter_words = [word for word in words if len(word) > limit]
    print(filter_words)

def main(argc, argv):
    if argc != 3 or not argv[2].isdigit():
        error_message()
    else:
        filterInput(argv[1], int(argv[2]))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)