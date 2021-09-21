import argparse

import pandas as pd

parser = argparse.ArgumentParser(description='Converts biobank files to nparACT format. Removes unecessary columns.')
parser.add_argument('directory', help='directory with the biobank csvs (no trailing slash)')
args = parser.parse_args()
path = args.directory
filename = path.split("\\")[-1]
df = pd.read_csv(path)

for i in range(len(df["time"])):
    date = str(df.at[i, "time"]).split(" ")[0]
    # date = str(str(date).replace("-", "/"))
    t = str(df.at[i, "time"]).split(" ")[1].split(".")[0]
    df.at[i, "time"] = f"{date} {t}"

# 2014-05-29T10:15:00-0700
df = df.drop(["imputed", "MVPA", "light", "sedentary", "sleep", "MET"], axis=1)

df.to_csv(path + "//" + "nparactformat_" + filename, header=False, index=False)
