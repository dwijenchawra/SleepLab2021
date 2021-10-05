from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from tqdm import tqdm

# original = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\biobank_nparACTPreppedFiles\IVIS_data_ORIGINAL.csv"
# imputed = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_imputed\ukbb_imputed IVIS_data_imputed.csv"
# masked = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_masked\ukbb_masked IVIS_data_masked.csv"

original = r"C:\Users\dwije\PycharmProjects\GGIRanalysis\biobank_nparACTPreppedFiles\IVIS_data_ORIGINAL.csv"
imputed = r"C:\Users\dwije\PycharmProjects\GGIRanalysis\ukbb_imputed\ukbb_imputed IVIS_data_imputed.csv"
masked = r"C:\Users\dwije\PycharmProjects\GGIRanalysis\ukbb_masked\ukbb_masked IVIS_data_masked.csv"

maskCount = 30

imputedcsv = pd.read_csv(imputed)
maskedcsv = pd.read_csv(masked)
originalcsv = pd.read_csv(original)

repeatedOrig = pd.DataFrame(columns=["ORIGINAL IS", "ORIGINAL IV"])

for i in tqdm(range(len(originalcsv.iloc[:, 1]))):  # is 1 iv 2
    for j in range(maskCount):
        repeatedOrig.loc[len(repeatedOrig)] = list(originalcsv.iloc[i, 1:3])

maskedcsv = maskedcsv.rename(columns={"IS": "MASKED IS", "IV": "MASKED IV"})
imputedcsv = imputedcsv.rename(columns={"IS": "IMPUTED IS", "IV": "IMPUTED IV"})
repeatedOrig = repeatedOrig.join(maskedcsv["MASKED IS"])
repeatedOrig = repeatedOrig.join(maskedcsv["MASKED IV"])
repeatedOrig = repeatedOrig.join(imputedcsv["IMPUTED IS"])
repeatedOrig = repeatedOrig.join(imputedcsv["IMPUTED IV"])
repeatedOrig = repeatedOrig.join(imputedcsv["Mask Length"])
repeatedOrig = repeatedOrig.join(imputedcsv["Weekday"])

# = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
maskcol = []

masks = list(dict.fromkeys(repeatedOrig["Mask Length"]))
masks.remove("ZERODIVBLANK")
days = list(dict.fromkeys(repeatedOrig["Weekday"]))
days.remove("WEEK")
print(len(masks) * len(days))


def plotter(axis, col1, col2, mask, day, title):
    fig = plt.Figure(figsize=(14, 10))
    ax = fig.add_subplot(111)

    # canvas = FigureCanvas(fig)
    # canvas.print_figure('plots/' + str(i.split("\\")[-1]) + ".png")

    try:
        plot = sm.graphics.mean_diff_plot(col1, col2, ax=ax)
        plt.title(title)
        plt.tight_layout()
        canvas = FigureCanvas(fig)
        canvas.print_figure('plots/' + title + ".png", bbox_inches="tight")
    except ValueError:
        # print(col1)
        # print(col2)
        # sleep(20)
        pass

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
        maskdf = repeatedOrig.loc[repeatedOrig['Mask Length'] == mask]
        maskdaydf = maskdf.loc[maskdf['Weekday'] == day]
        # print(maskdaydf)
        # print("\n\n\n\n")
        fig, ax = plt.subplots()

        print(f"{mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day,
        #         f"Original vs Imputed IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day,
        #         f"Original vs Imputed IV {mask} {day}")
        #
        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day,
                     f"Original vs Masked IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day,
                     f"Original vs Masked IV {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day,
                     f"Original vs Imputed IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day,
                     f"Original vs Imputed IV {mask} {day}")

for mask in ["10-12", "18-20"]:
    for day in ["WEEK"]:
        maskdf = repeatedOrig.loc[repeatedOrig['Mask Length'] == mask]
        maskdaydf = maskdf.loc[maskdf['Weekday'] == day]
        # print(maskdaydf)
        # print("\n\n\n\n")
        fig, ax = plt.subplots()

        print(f"{mask} {day}")
        plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day, f"Original vs Masked IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day, f"Original vs Masked IV {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day,
        #         f"Original vs Imputed IS {mask} {day}")
        # plotter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day,
        #         f"Original vs Imputed IV {mask} {day}")
        #
        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["MASKED IS"], mask, day,
                     f"Original vs Masked IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["MASKED IV"], mask, day,
                     f"Original vs Masked IV {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IS"], maskdaydf["IMPUTED IS"], mask, day,
                     f"Original vs Imputed IS {mask} {day}")
        statsPrinter(ax, maskdaydf["ORIGINAL IV"], maskdaydf["IMPUTED IV"], mask, day,
                     f"Original vs Imputed IV {mask} {day}")

pprint(infodf)
infodf.to_csv("blandaltman_stats.csv", index=False)