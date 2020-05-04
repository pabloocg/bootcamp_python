def generator(text:str, sep=" ", option=None) -> str:
    '''Option is an optional arg, sep is mandatory'''

    if not isinstance(text, str) or (option != None and option != "shuffle" and option != "unique" and option != "ordered"):
        exit("ERROR")
    if option == "shuffle":
        text_splited = set(text.split(sep))
    elif option == "unique":
        text_splited = text.split(sep)
        new_list = []
        [new_list.append(i) for i in text_splited if i not in new_list]
        text_splited = new_list
    elif option == "ordered":
        text_splited = text.split(sep)
        text_splited = sorted(text_splited)
    else:
        text_splited = text.split(sep)
    for word in text_splited:
        yield word

def main():
    text = "Le Lorem Ipsum est simplement du faux texte."
    print("Normal iteration:")
    for word in generator(text, sep=" "):
        print(word, end= " ")
    print("\nShuffle iteration:")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word, end= " ")
    print("\nOrdered iteration:")
    for word in generator(text, sep=" ", option="ordered"):
        print(word, end= " ")
    text = "Le Le Le Le Lorem Ipsum Ipsum Ipsum est simplement du faux texte."
    print("\nUnique iteration:")
    for word in generator(text, sep=" ", option="unique"):
        print(word, end= " ")

if __name__ == "__main__":
    main()