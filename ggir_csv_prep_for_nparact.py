import time

import pandas as pd


# df = pd.read_csv("1001787_90001_0_0.cwa.RData.csv")
def convertForNPARact(path):
    df = pd.read_csv(path)

    for i in range(len(df["timestamp"])):
        date = str(df.at[i, "timestamp"]).split("T")[0]
        date = str(str(date).replace("-", "/"))
        t = str(df.at[i, "timestamp"]).split("T")[1].removesuffix("-0700")
        df.at[i, "timestamp"] = f"{date} {t}"

    # 2014-05-29T10:15:00-0700
    df = df.drop(["ENMO"], axis=1)
    # print(df)
    # print(df.isnull().sum().sum())
    # df.to_csv("nparacttest/ggir_imputed.csv", header=False, index=False)
    df.to_csv("nparacttest/python_imputed.csv", header=False, index=False)
