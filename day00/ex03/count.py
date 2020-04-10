import string

def text_analyzer(*text):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''

    lower_count = lambda txt: sum(1 for char in txt if char.islower())
    upper_count = lambda txt: sum(1 for char in txt if char.isupper())
    marks_count = lambda txt, marks: sum(1 for char in txt if char in marks)

    if len(text) == 1 and len(text[0]) > 0:
        to_analize = text[0]
    elif len(text) == 0:
        to_analize = input("What is the text to analyse?\n")
    else:
        print("ERROR")
        exit(1)
    print ("The text contains " + str(len(to_analize)) + " characters:")
    print ("- " + str(upper_count(to_analize)) + " upper letters")
    print ("- " + str(lower_count(to_analize)) + " lower letters")
    print ("- " + str(marks_count(to_analize, string.punctuation)) + " punctuation marks")
    print ("- " + str(to_analize.count(' ')) + " spaces")
