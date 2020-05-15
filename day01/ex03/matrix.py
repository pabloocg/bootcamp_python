from vector import Vector

class Matrix(object):
    def __init__(self, initData: (list, tuple)):
        if isinstance(initData, list):
            self.data = initData
            self.shape = (len(self.data), len(self.data[0]))
        elif isinstance(initData, tuple):
            self.shape = initData
            self.data = []
            begin = 0
            end = initData[1]
            for j in range(initData[0]):
                self.data.append([float(i) for i in range(begin, end)])
                begin = initData[1] + begin
                end += initData[1]

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) != len(other.data):
                return None
            matrixData = []
            for myMatrix, otherMatrix in zip(self.data, other.data):
                matrixData.append([(mydata + otherdata) for mydata, otherdata in zip(myMatrix, otherMatrix)])
            return Matrix(matrixData)
        elif isinstance(other, Vector):
            if len(self.data) != other.size:
                return None
            matrixData = []
            for myMatrix, vectorData in zip(self.data, other.values):
                matrixData.append([(mydata + vectorData) for mydata in myMatrix])
            return Matrix(matrixData)

    def __radd__(self, other):
        return Matrix.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) != len(other.data):
                return None
            matrixData = []
            for myMatrix, otherMatrix in zip(self.data, other.data):
                matrixData.append([(mydata - otherdata) for mydata, otherdata in zip(myMatrix, otherMatrix)])
            return Matrix(matrixData)
        elif isinstance(other, Vector):
            if len(self.data) != other.size:
                return None
            matrixData = []
            for myMatrix, vectorData in zip(self.data, other.values):
                matrixData.append([(mydata - vectorData) for mydata in myMatrix])
            return Matrix(matrixData)

    def __rsub__(self, other):
        return Matrix.__sub__(self, other)

    def __truediv__(self, other):
        if isinstance(other, int):
            matrixData = []
            for myMatrix in self.data:
                matrixData.append([(mydata / other) for mydata in myMatrix])
            return Matrix(matrixData)

    def __rtruediv__(self, other):
        return Matrix.__truediv__(self, other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.data) != len(other.data):
                return None
            matrixData = []
            for myMatrix, otherMatrix in zip(self.data, other.data):
                matrixData.append([(mydata * otherdata) for mydata, otherdata in zip(myMatrix, otherMatrix)])
            return Matrix(matrixData)
        elif isinstance(other, int):
            matrixData = []
            for myMatrix in self.data:
                matrixData.append([(mydata * other) for mydata in myMatrix])
            return Matrix(matrixData)
        elif isinstance(other, Vector):
            if len(self.data) != other.size:
                return None
            vector_values = []
            for myMatrix, vectorValue in zip(self.data, other.values):
                val = 0
                for mydata in myMatrix:
                    val += (mydata * vectorValue)
                vector_values.append(val)
            return Vector(vector_values)

    def __rmul__(self, other):
        return Matrix.__mul__(self, other)

    def __str__(self):
        return f"Matrix data: {self.data}\nshape: {self.shape}"

    def __repr__(self):
        return f"Matrix{self.shape} {self.data}"
                