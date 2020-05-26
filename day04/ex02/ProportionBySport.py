from FileLoader import FileLoader
import pandas as pd


def proportionBySport(df: pd.DataFrame, oyear: int, sport: str, gender: chr) -> float:
    total = df.Name[(df.Year == oyear) & (df.Sex == gender)].drop_duplicates().count()
    data = df.Name[(df.Year == oyear) & (df.Sex == gender) & (df.Sport == sport)].drop_duplicates().count()
    return data / total


def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    prop = proportionBySport(data, 2012, 'Tennis', 'M')
    print(prop)


if __name__ == "__main__":
    main()