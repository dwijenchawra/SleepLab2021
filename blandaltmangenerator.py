from pprint import pprint

import numpy as np
import statsmodels.api as sm
import pandas as pd

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import statsmodels.stats.descriptivestats

original = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\biobank_nparACTPreppedFiles\IVIS_data_ORIGINAL.csv"
imputed = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_imputed\ukbb_imputed IVIS_data_imputed.csv"
masked = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_masked\ukbb_masked IVIS_data_masked.csv"

imputedcsv = pd.read_csv(imputed)
maskedcsv = pd.read_csv(masked)
originalcsv = pd.read_csv(original)


# = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
maskcol = []

masks = list(dict.fromkeys(masked["Mask Length"]))
days = list(dict.fromkeys(masked["Weekday"]))
print(len(masks) * len(days))


def plotter(axis, col1, col2, mask, day, title):

    fig = plt.Figure(figsize=(14, 10))
    ax = fig.add_subplot(111)

    canvas = FigureCanvas(fig)
    canvas.print_figure('testerplots/' + str(i.split("\\")[-1]) + ".png")

    plot = sm.graphics.mean_diff_plot(col1, col2, ax=ax)
    plt.title(title)
    plt.tight_layout()
    canvas = FigureCanvas(fig)
    canvas.print_figure('plots/' + + "\\" + title + ".png", bbox_inches="tight")
    # plot.savefig(r"C:\Users\Jamie\PycharmProjects\SleepLab2021\plots" + "\\" + title + ".png", bbox_inches="tight")
    # # plt.show()
    # axis.cla()

infodf = pd.DataFrame(columns=["title", "std_dev", "mean"])

def statsPrinter(ax, m1, m2, mask, day, title):
    diffs = m1 - m2
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs, axis=0)
    # print(title + "    " + str(std_diff))
    infodf.loc[len(infodf)] = [title, std_diff, mean_diff]

for mask in masks:
    for day in days:
        maskdf = STATSCSV.loc[STATSCSV['Mask Length'] == mask]
        maskdaydf = maskdf.loc[maskdf['Weekday'] == day]
        # print(maskdaydf)
        # print("\n\n\n\n")
        fig, ax = plt.subplots()

        print(f"{mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day, f"Original vs Imputed IS {mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day, f"Original vs Imputed IV {mask} {day}")
        #
        # statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        # statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        # statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day, f"Original vs Imputed IS {mask} {day}")
        # statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day, f"Original vs Imputed IV {mask} {day}")

pprint(infodf)
infodf.to_csv("blandaltman_stats.csv", index=False)