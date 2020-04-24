def kataDicc(d):
    for elem, key in d.items():
        print(f"{elem} was created by {key}")

def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf'
    }
    kataDicc(languages)

if __name__ == "__main__":
    main()
