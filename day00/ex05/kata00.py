def kataTuple(t):
    contentTuple = ", ".join([str(i) for i in t])
    print(f"The {len(t)} numbers are: {contentTuple}")

def main():
    t = (34, 56, 79)
    kataTuple(t)
    t = (34, 56, 79, 90, 2, 45)
    kataTuple(t)
    t = (34, 56, 79, 90, 2, 45, 34, 56, 79, 90, 2, 45, 34, 56, 79, 90, 2, 45)
    kataTuple(t)

if __name__ == "__main__":
    main()