import pandas as pd

IMPUTE_CSV = "Andrew_M-timeSeries.csv"

# 2021-05-03 16:12:49.619000+0100 [Europe/London]

df = pd.read_csv(IMPUTE_CSV)

timestamps = df['time']
imputed = df['imputed']

zipdict = dict(zip(timestamps, imputed))

parseable = [[int(str(timestamps[i]).split(" ")[0].split("-")[2]), imputed[i]] for i in range(len(timestamps))]

final = []

prev = parseable[0][0]
sum = 0
count = 0

for i in range(0, len(parseable)):
    count += 1
    if parseable[i][0] != prev:
        prev = parseable[i][0]
        ratio = sum / count
        if ratio < 0.5:
            final.extend(parseable[i - (count - 1):i])
        sum = 0
        count = 0
    sum += parseable[i][1]


