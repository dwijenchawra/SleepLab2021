import statsmodels
import pandas as pd

stats = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\COMPLETE_IVIS_STATS_withmasks.csv"
STATSCSV = pd.read_csv(stats)

# = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
maskcol = []

masks = list(dict.fromkeys(STATSCSV["Mask"]))
days = list(dict.fromkeys(STATSCSV["Weekday"]))

for mask in masks:
    for day in days:
        maskdf = STATSCSV.loc[STATSCSV['Mask'] == mask]
        maskdaydf = maskdf.loc[maskdf['Weekday'] == day]
        # print(maskdaydf)
        # print("\n\n\n\n")


