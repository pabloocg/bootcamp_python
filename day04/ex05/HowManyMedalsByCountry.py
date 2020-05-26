from FileLoader import FileLoader
import pandas as pd

def howManyMedalsByCountry(df: pd.DataFrame, city: str) -> dict:
    medals = df.query('City == @city').sort_values(by='Year')[['Year', 'Medal']]
    ret = {}
    for _, data in medals.iterrows():
        ret[data['Year']] = {'G': 0, 'S': 0, 'B': 0}
    for _, data in medals.iterrows():
        if data['Medal'] == 'Gold':
            ret[data['Year']]['G'] += 1
        elif data['Medal'] == 'Silver':
            ret[data['Year']]['S'] += 1
        elif data['Medal'] == 'Bronze':
            ret[data['Year']]['B'] += 1
    return ret


def main():
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    std = howManyMedalsByCountry(data, 'London')
    print(std)


if __name__ == "__main__":
    main()
