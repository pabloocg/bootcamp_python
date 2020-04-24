def kataDate(t):
    print(f"{t[3]:02}/{t[4]:02}/{t[2]:02} {t[0]:02}:{t[1]:02}")

def main():
    t = (3, 30, 2019, 9, 25)
    kataDate(t)
    t = (00, 00, 2019, 9, 25)
    kataDate(t)
    t = (15, 2, 2020, 16, 30)
    kataDate(t)

if __name__ == "__main__":
    main()