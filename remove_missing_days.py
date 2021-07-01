import pandas as pd

IMPUTE_CSV = "Andrew_M-timeSeries.csv"

# 2021-05-03 16:12:49.619000+0100 [Europe/London]

def revertTime(year, month, day, hour, minute, second):
    return f"{year}-{month}-{day} {hour}:{minute}:{second}.619000+0100 [Europe/London]"

df = pd.read_csv(IMPUTE_CSV)

timestamps = df['time']
imputed = df['imputed']

print("making parseable")

parseable = [
    [list(map(int, str(timestamps[i]).split(" ")[0].split("-"))),
     list(map(int, str(timestamps[i]).split(" ")[1].split(".")[0].split(":"))),
     imputed[i],
     df["acc"][i],
     df["MVPA"][i],
     df["light"][i],
     df["sedentary"][i],
     df["sleep"][i],
     df["MET"][i]]
    for i in range(len(timestamps))]

final = []

prev = parseable[0][0][2]
sum = 0
count = 0

print("starting loop")

for i in range(0, len(parseable)):
    count += 1
    if parseable[i][0][2] != prev:
        prev = parseable[i][0][2]
        ratio = sum / count
        if ratio < 0.5:
            final.extend(parseable[i - (count - 1):i])
        sum = 0
        count = 0
    sum += parseable[i][2]

def revertList(data):
    return [[revertTime(i[0][0], i[0][1], i[0][2], i[1][0], i[1][1], i[1][2])] + i[2:] for i in data]

print("creating export list")

export = revertList(final)
pass
