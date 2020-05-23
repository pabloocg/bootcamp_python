import numpy as np
import math
import random
from csvreader import CsvReader
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def get_random_data(self, data) -> np.array:
        ret = np.zeros(shape=(self.ncentroid, 4))
        rand = 0
        limit = inc = int((data.shape[0] - 1) / self.ncentroid)
        for i in range(self.ncentroid):
            ret[i] = data[random.randint(rand, limit)]
            rand += inc
            limit += inc
        return np.array(ret[:, 1:])

    def euclidean_distance(self, a, b):
        return np.sqrt(np.sum(np.power(a - b, 2)))
    
    def fit(self, data) -> None:
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        self.centroids = self.get_random_data(data)
        data = data[:, 1:]
        for _ in range(self.max_iter):
            self.classes = {}
            for i in range(self.ncentroid):
                self.classes[i] = []
            for citiziens in data:
                distances = [self.euclidean_distance(citiziens, centroid) for centroid in self.centroids]
                nucleus = distances.index(min(distances))
                self.classes[nucleus].append(citiziens)
            for i in self.classes:
                self.centroids[i] = np.average(self.classes[i], axis=0)

    def predict(self, data) -> np.array:
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
          This function should not raise any Exception.
        """
        planets = ['The flying cities of Venus', 'United Nations of Earth', 'Mars Republic', 'Asteroids Belt colonies']
        ret = np.chararray(shape=(data.shape[0], 2), itemsize=26)
        data = data[:, 1:]
        for i, citiziens in enumerate(data):
            distances = [self.euclidean_distance(citiziens, centroid) for centroid in self.centroids]
            idx = distances.index(min(distances))
            ret[i][0] = i
            ret[i][1] = planets[idx]
        return ret


def main():
    km = KmeansClustering(max_iter=100)
    with CsvReader('../resources/solar_system_census.csv') as file:
        if file == None:
            exit("File is corrupted")
        dataset = file.getdata()
    dataset = np.array(dataset, dtype='float')
    km.fit(dataset)
    print(km.predict(dataset))

    colors = 10*["r", "g", "c", "b", "k"]
    for centroid in km.centroids:
        plt.scatter(centroid[0], centroid[1], s = 130, marker = "x")
    for classification in range(len(km.classes)):
        color = colors[classification]
        for citiziens in km.classes[classification]:
            plt.scatter(citiziens[0], citiziens[1], color = color,s = 30)
    plt.show()


if __name__ == "__main__":
    main()
