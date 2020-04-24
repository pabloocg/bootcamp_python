def kataNumbers(t):
    print(f"day{t[0]:02}, ex_{t[1]:02} : {round(t[2], 2)}, {t[3]:.2e}, {t[4]:.2e}")

def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    kataNumbers(t)

if __name__ == "__main__":
    main()