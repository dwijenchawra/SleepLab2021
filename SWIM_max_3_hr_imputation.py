import pandas as pd
import os

os.chdir(r"C:\Users\lab\Desktop\SWIMAccelerometerData")


for swimmer in [10]:
    IMPUTE_CSV = 'SWIM' + str(swimmer) + '-timeSeries.csv'
    print('Gathering data for swimmer ' + str(swimmer) + ' -- this should not take more than a moment...')
    # 2021-05-03 16:12:49.619000+0100 [Europe/London]

    def revertTime(year, month, day, hour, minute, second):
        return f"{year}-{month}-{day} {hour}:{minute}:{second}"  ## the .619... part is specific to one swimmer, eliminate

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
    max_minutes_imputed = 180
    imputation_limit = max_minutes_imputed / 1440  # maximum permissible imputed min divided by total min in day

    print("starting data loop for swimmer " + str(swimmer))

    for i in range(0, len(parseable)):
        count += 1
        if parseable[i][0][2] != prev:
            prev = parseable[i][0][2]
            ratio = sum / count
            if ratio < imputation_limit:
                final.extend(parseable[i - (count - 1):i])
            sum = 0
            count = 0
        sum += parseable[i][2]

    def revertList(data):
        return [[revertTime(i[0][0], i[0][1], i[0][2], i[1][0], i[1][1], i[1][2])] + i[2:] for i in data]

    print("creating new csv file")
    export = revertList(final)
    df = pd.DataFrame(export)
    df.columns = ['time', 'imputed', 'acc', 'MVPA', 'light', 'sedentary', 'sleep', 'MET']
    df.to_csv(r"C:\Users\lab\Desktop\SWIMAccelerometerData\Less_than_3_hr_imputed\SWIM" +
              str(swimmer) + '-less_than_3hr_imputed--test.csv', index=False)
pass
