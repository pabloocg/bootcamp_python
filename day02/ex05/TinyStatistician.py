import math


class TinyStatistician(object):

    def isEmpty(self, arr: list or tuple) -> bool:
        if arr is None or not len(arr):
            return True
        return False

    def mean(self, arr: list or tuple) -> float:
        if self.isEmpty(arr):
            return None
        ret = 0.0
        for n in arr:
            ret += n
        return float(ret / len(arr))

    def median(self, arr: list or tuple) -> float:
        if self.isEmpty(arr):
            return None
        arr.sort()
        if len(arr) % 2 == 0:
            return float((arr[int(len(arr) / 2)] +
                         arr[int(len(arr) / 2) - 1]) / 2)
        else:
            return float(arr[int(len(arr) / 2)])

    def quartiles(self, arr: list or tuple, percentile: int) -> float:
        if self.isEmpty(arr):
            return None
        arr.sort()
        if percentile == 25:
            indexf = (len(arr) + 3) / 4
        else:
            indexf = (3 * len(arr) + 1) / 4
        if indexf - int(indexf) > 0.0:
            return float(arr[int(indexf) - 1] + ((indexf - int(indexf)) *
                         (arr[int(indexf)] - arr[int(indexf) - 1])))
        else:
            return float(arr[int(indexf) - 1])

    def var(self, arr: list or tuple) -> float:
        meanf = self.mean(arr)
        if meanf is None:
            return None
        ret = 0.0
        for n in arr:
            ret += (n - meanf) * (n - meanf)
        return float(ret / len(arr))

    def std(self, arr: list or tuple) -> float:
        varRes = self.var(arr)
        return math.sqrt(varRes) if varRes else None


def main():
    Calc = TinyStatistician()
    arr = [i for i in range(10)]
    print(f"mean: {Calc.mean(arr)}")
    arr = [3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29]
    print(f"median: {Calc.median(arr)}")
    arr = [1, 42, 300, 10, 59]
    print(f"quartile: {Calc.quartiles(arr, 25)}")
    print(f"quartile: {Calc.quartiles(arr, 75)}")
    print(f"variance: {Calc.var(arr)}")
    print(f"std: {Calc.std(arr)}")


if __name__ == "__main__":
    main()
