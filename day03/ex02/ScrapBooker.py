from ImageProcessor import ImageProcessor
import numpy as np


class ScrapBooker(object):

    def crop(self, array, dimensions: tuple, position=(0, 0)):

        w, h = dimensions
        x, y = position
        if w + x > len(array) or h + y > len(array[0]):
            exit("New size image error.")
        print(f"perform crop widht {w} height {h}")
        newArray = array[x:, y:]
        return newArray[:w, :h]

    def thin(self, array, n: int, axis: int):

        print(f"perform thin with n={n} and axis={axis}:")
        if n < 2:
            return array
        if axis == 0:
            tmp = np.array(range(1, len(array[0]) + 1))
            return array[:, (tmp % n != 0)]
        else:
            tmp = np.array(range(1, len(array) + 1))
            return array[(tmp % n != 0), :]

    def juxtapose(self, array, n: int, axis: int):

        copy = array.copy()
        for _ in range(n):
            array = np.concatenate((array, copy), axis)
        return array

    def mosaic(self, array, dimensions: tuple):

        copy = array.copy()
        w, h = dimensions
        for _ in range(h - 1):
            array = np.concatenate((array, copy), 1)
        copy = array.copy()
        for _ in range(w - 1):
            array = np.concatenate((array, copy), 0)
        return array


def main():
    img = ImageProcessor()
    slic = ScrapBooker()
    array = img.load("../resources/42AI.png")
    retArray = slic.crop(array, (200, 100))
    img.display(retArray)
    retArray = slic.thin(array, 4, 0)
    img.display(retArray)
    retArray = slic.juxtapose(array, 3, 0)
    img.display(retArray)
    retArray = slic.mosaic(array, (10, 4))
    img.display(retArray)


if __name__ == "__main__":
    main()
