from FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData(object):
    def __init__(self, df: pd.DataFrame):
        self.dataframe = df

    def when(self, location: str) -> list:
        ret = self.dataframe.query('City == @location')['Year'].drop_duplicates()
        return ret.to_list()

    def where(self, date: int) -> list:
        ret = self.dataframe.query('Year == @date')['City'].drop_duplicates()
        return ret.to_list()


def main():
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    std = SpatioTemporalData(data)
    print(std.where(2016))
    print(std.when('Paris'))


if __name__ == "__main__":
    main()
