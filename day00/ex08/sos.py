import sys

def check_string(txt):
    for char in txt:
        if not char.isalpha() and not char.isspace() and not char.isdigit():
            return False
    return True

def parse_morse(txt):
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", " ": " ", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    return " ".join(morse.get(char) for char in txt)

if __name__ == "__main__":

    [sys.exit("ERROR") for i in range(1, len(sys.argv)) if not check_string(sys.argv[i])]
    if (len(sys.argv) > 1):
        print(" / ".join(parse_morse(sys.argv[i].upper()) for i in range(1, len(sys.argv))))