from FileLoader import FileLoader
import pandas as pd


def youngestFellah(df: pd.DataFrame, year: int) -> dict:
    m = df.Age[(df.Year == year) & (df.Sex == "M")].min()
    f = df.Age[(df.Year == year) & (df.Sex == "F")].min()
    return {'Age-female': f, 'Age-male': m}


def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    dic = youngestFellah(data, 2012)
    print(dic)


if __name__ == "__main__":
    main()
