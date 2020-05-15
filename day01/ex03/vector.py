class Vector:
    def __init__(self, param):
        if isinstance(param, list):
            self.values = param
            self.size = len(self.values)
        elif isinstance(param, int):
            self.size = param
            self.values = [float(i) for i in range(param)]
        elif isinstance(param, range):
            self.values = [float(i) for i in param]
            self.size = len(self.values)
        elif isinstance(param, Vector):
            self.values = param.values
            self.size = param.size

    def __add__(self, other):
        if isinstance(other, Vector):
            vector_values = [(value + value_other) for value, value_other in zip(self.values, other.values)]
        else:
            vector_values = [(value + other) for value in self.values]
        return Vector(vector_values)

    def __radd__(self, other):
        return Vector.__add__(self, other)

    def __iadd__(self, other):
        self = Vector.__add__(self, other)
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            vector_values = [(value - value_other) for value, value_other in zip(self.values, other.values)]
        else:
            vector_values = [(value - other) for value in self.values]
        return Vector(vector_values)

    def __rsub__(self, other):
        return Vector.__sub__(self, other)

    def __isub__(self, other):
        self = Vector.__sub__(self, other)
        return self

    def __truediv__(self, other):
        try:
            if isinstance(other, Vector):
                vector_values = [(value / value_other) for value, value_other in zip(self.values, other.values)]
            else:
                vector_values = [(value / other) for value in self.values]
        except ZeroDivisionError:
            print("ERROR (division by zero)")
        else:
            return Vector(vector_values)
        return None

    def __rtruediv__(self, other):
        return Vector.__truediv__(self, other)

    def __itruediv__(self, other):
        self = Vector.__truediv__(self, other)
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            vector_values = [(value * value_other) for value, value_other in zip(self.values, other.values)]
        else:
            vector_values = [(value * other) for value in self.values]
        return Vector(vector_values)

    def __rmul__(self, other):
        return Vector.__mul__(self, other)
    
    def __imul__(self, other):
        self = Vector.__mul__(self, other)
        return self

    def __str__(self) -> str:
        return f"{self.values}"

    def __repr__(self) -> str:
        return f"({self.__class__.__name__} {self.values})"
