import pandas as pd


class FileLoader(object):
    @staticmethod
    def load(path: str) -> pd.DataFrame:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape[0], "x", data.shape[1])
        return data

    @staticmethod
    def display(df, n):
        if n > 0:
            print(df.iloc[:n])
        else:
            print(df.iloc[n:])


def main():
    loader = FileLoader()
    data = loader.load("../resources/adult_data.csv")
    loader.display(data, 12)


if __name__ == "__main__":
    main()
