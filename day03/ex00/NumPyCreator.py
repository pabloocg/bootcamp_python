import numpy as np


class NumPyCreator(object):

    def from_list(self, lst, dtype=None):
        return np.array(lst, dtype)

    def from_tuple(self, tpl, dtype=None):
        return self.from_list(tpl, dtype)

    def from_iterable(self, itr, dtype=int):
        return np.fromiter(itr, dtype)

    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    def random(self, shape, dtype=float):
        return np.empty(shape, dtype)

    def identity(self, n, dtype=float):
        return np.eye(n, dtype=dtype)


def main():
    npc = NumPyCreator()
    lstArray = npc.from_list([[1, 2, 3], [6, 3, 4]])
    print("Array from list: ")
    print(lstArray)
    tplArray = npc.from_tuple(("a", "b", "c"))
    print("Array from tuple: ")
    print(tplArray)
    iterArray = npc.from_iterable(range(10))
    print("Array from iterable: ")
    print(iterArray)
    shapeArray = npc.from_shape((3, 5), 5)
    print("Array from shape: ")
    print(shapeArray)
    randomArray = npc.random((3, 5))
    print("Array from shape with random values: ")
    print(randomArray)
    eyeArray = npc.identity(5)
    print("Array from shape with eye format: ")
    print(eyeArray)


if __name__ == "__main__":
    main()
