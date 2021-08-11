from pprint import pprint

import numpy as np
import statsmodels.api as sm
import pandas as pd
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statsmodels.stats.descriptivestats

stats = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\COMPLETE_IVIS_STATS_withmasks.csv"
STATSCSV = pd.read_csv(stats)

# = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
maskcol = []

masks = list(dict.fromkeys(STATSCSV["Mask"]))
days = list(dict.fromkeys(STATSCSV["Weekday"]))
print(len(masks) * len(days))


def plotter(axis, col1, col2, mask, day, title):
    plot = sm.graphics.mean_diff_plot(col1, col2, ax=axis)
    plt.title(title)
    plt.tight_layout()
    plot.savefig(r"C:\Users\Jamie\PycharmProjects\SleepLab2021\plots" + "\\" + title + ".png", bbox_inches="tight")
    # plt.show()
    axis.cla()

infodf = pd.DataFrame(columns=["title", "std_dev", "mean"])

def statsPrinter(ax, m1, m2, mask, day, title):
    diffs = m1 - m2
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs, axis=0)
    # print(title + "    " + str(std_diff))
    infodf.loc[len(infodf)] = [title, std_diff, mean_diff]

for mask in masks:
    for day in days:
        maskdf = STATSCSV.loc[STATSCSV['Mask'] == mask]
        maskdaydf = maskdf.loc[maskdf['Weekday'] == day]
        # print(maskdaydf)
        # print("\n\n\n\n")
        fig, ax = plt.subplots()

        print(f"{mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day, f"Original vs Imputed IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day, f"Original vs Imputed IV {mask} {day}")

        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day, f"Original vs Imputed IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day, f"Original vs Imputed IV {mask} {day}")

pprint(infodf)
infodf.to_csv("blandaltman_stats.csv", index=False)