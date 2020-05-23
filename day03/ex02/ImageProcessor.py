from matplotlib import pyplot as plt


class ImageProcessor(object):

    def load(self, path: str):
        try:
            image = plt.imread(path)
        except FileNotFoundError:
            exit(f"File {path} not found.")
        else:
            print(f"Loading image of dimensions {len(image)} \
                x {len(image[0])}")
            return image

    def display(self, array):
        plt.imshow(array)
        plt.show()


def main():
    img = ImageProcessor()
    arr = img.load("../assets/blue.png")
    img.display(arr)


if __name__ == "__main__":
    main()
