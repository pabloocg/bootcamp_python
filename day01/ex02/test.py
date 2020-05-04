from vector import Vector


def main():
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v1)
    v1 = Vector(7)
    print(repr(v1))
    v1 = Vector(range(10, 15))
    print(v1)
    v1 = v1 + 5
    print(v1)
    v2 = 5 + v1
    print(v2)
    v3 = v2 + v1
    print(v3)
    v3 = v2 / 0
    print(v3)
    v3 = v1 - v2
    print(v3)

    v3 *= 20
    print(v3)

if __name__ == "__main__":
    main()