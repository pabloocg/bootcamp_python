from ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter(object):

    @staticmethod
    def invert(array):
        array[:, :, :3] = 1. - array[:, :, :3]
        return array

    def to_blue(self, array):
        array[:, :, :2] = np.zeros(array.shape)[:, :, :2]
        return array

    def to_green(self, array):
        array[:, :, 0:3:2] *= 0
        return array

    def to_red(self, array):
        array[:, :, 0:3] -= self.to_blue(array.copy())[:, :, 0:3] \
            + self.to_green(array.copy())[:, :, 0:3]
        return array

    def shadow(self, a, b):
        return b * int(a / b)

    def celluloid(self, array, nthresholds=4):
        vfunc = np.vectorize(self.shadow)
        array[:, :, :3] = vfunc(array[:, :, :3], 1.0 / nthresholds)
        return array

    @staticmethod
    def to_grayscale(array, filter='weighted'):
        if filter == 'weighted' or filter == 'w':
            array[:, :, :1] *= 0.299
            array[:, :, 1:2] *= 0.587
            array[:, :, 2:3] *= 0.114
            sumrgb = np.sum(array[:, :, :3], axis=2, keepdims=True)
            array[:, :, :3] = np.tile(sumrgb, reps=(1, 3))
        elif filter == 'mean' or filter == 'm':
            sumrgb = np.sum(array[:, :, :3], axis=2, keepdims=True) / 3
            sumrgb = np.broadcast_to(sumrgb, array.shape)
            array[:, :, :3] = sumrgb[:, :, :3]
        return array


def main():
    img = ImageProcessor()
    cf = ColorFilter()
    array = img.load("../assets/img.png")
    retArray = cf.to_grayscale(array, filter='mean')
    img.display(retArray)


if __name__ == "__main__":
    main()
