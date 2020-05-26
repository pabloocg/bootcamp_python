import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader
import seaborn as sns


class MyPlotLib(object):
    @staticmethod
    def histogram(data: pd.DataFrame, features: list):
        ax = data.hist(column=features, grid=False, color='#86bf91', zorder=2, rwidth=0.9)
        ax = ax[0]
        for i, x in enumerate(ax):
            x.spines['right'].set_visible(False)
            x.spines['top'].set_visible(False)
            x.spines['left'].set_visible(False)
            x.set_title("")
            x.set_xlabel(features[i], weight='bold', size=12)
            x.set_ylabel("Quantity", labelpad=5, size=8)
        plt.show()

    @staticmethod
    def density(data: pd.DataFrame, features: list):
        for feat in features:
            sns.distplot(data[feat], hist=False, kde=True,
                        label=feat)
        plt.legend()
        plt.ylabel('Density')
        plt.xlabel('')
        plt.show()

    @staticmethod
    def pair_plot(data: pd.DataFrame, features: list):
        fig = plt.figure()
        ax2 = fig.add_subplot(222)
        ax1 = fig.add_subplot(221)
        ax4 = fig.add_subplot(224)
        ax3 = fig.add_subplot(223)
        ax1.hist(data[features[1]].dropna())
        ax1.set_ylabel(features[1])
        ax2.scatter(data[features[0]], data[features[1]], s=1, alpha=0.2)
        ax3.scatter(data[features[1]], data[features[0]], s=1, alpha=0.2)
        ax3.set_xlabel(features[1])
        ax3.set_ylabel(features[0])
        ax4.hist(data[features[0]].dropna())
        ax4.set_xlabel(features[0])
        plt.subplots_adjust(wspace=0.0, hspace=0.0)
        plt.show()

    @staticmethod
    def box_plot(data: pd.DataFrame, features: list):
        data.boxplot(column=features)
        plt.show()


def main():
    loader = FileLoader()
    mplt = MyPlotLib()
    data = loader.load("../resources/athlete_events.csv")
    #mplt.histogram(data, ['Height', 'Weight'])
    #mplt.density(data, ['Height', 'Weight'])
    #mplt.pair_plot(data, ['Height', 'Weight'])
    mplt.box_plot(data, ['Height', 'Weight'])


if __name__ == "__main__":
    main()
