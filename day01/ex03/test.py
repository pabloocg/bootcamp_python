from matrix import Matrix
from vector import Vector

def main():
    m3 = Matrix((3, 2))
    m4 = Matrix((3, 2))
    #print(m3)
    #print(m4)
    m5 = m3 + m4
    #print(m5)
    m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
    print(repr(m2))
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(repr(v1))
    m6 = m2 + v1
    #print(repr(m6))
    m7 = m2 * v1
    print(repr(m7))

if __name__ == "__main__":
    main()