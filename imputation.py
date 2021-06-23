import pandas as pd

IMPUTE_CSV = "F:\\ggir_missing_test\\out\\output_data\\meta\\csv\\1001787_90001_0_0.cwa.RData.csv"
starthour = "09"
startmin = "14"
startsec = "45"
endhour = "17"
endmin = "27"
endsec = "25"  # "20 + 5" for not including that one
missingdate = "2014-05-30".split("-")


# 2014-05-30T09:14:45-0700 start
# 2014-05-30T17:27:20-0700 end

def revertTime(year, month, day, hour, minute, second):
    return f"{year}-{month}-{day}T{hour}:{minute}:{second}-0700"


df = pd.read_csv(IMPUTE_CSV)

timestamps = df['timestamp']
anglez = df['anglez']

zipdict = dict(zip(timestamps, anglez))

parseable = [
    [str(timestamps[i]).removesuffix("-0700").split("T")[0].split("-"),
     str(timestamps[i]).removesuffix("-0700").split("T")[1].split(":")] for i
    in
    range(len(timestamps))]

condition = False
for i in range(len(parseable)):
    if parseable[i][0] == missingdate and parseable[i][1] == [starthour, startmin, startsec]:
        condition = True
    if parseable[i][0] == missingdate and parseable[i][1] == [endhour, endmin, endsec]:
        condition = False
    if condition:
        count = 0
        sum = 0
        for date in [["2014", "05", "29"], ["2014", "05", "31"], ["2014", "06", "01"], ["2014", "06", "02"],
                     ["2014", "06", "03"], ["2014", "06", "04"], ["2014", "06", "05"]]:
            reverted = revertTime(date[0], date[1], date[2], parseable[i][1][0], parseable[i][1][1], parseable[i][1][2])
            vector = zipdict.get(reverted)
            if vector is not None:
                sum += vector
                count += 1

        print(sum / count)
        print(count)
        anglez[i] = sum / count

df.to_csv("F:\\ggir_missing_test\\out\\output_data\\meta\\csv\\1001787_90001_0_0.cwa.RData.IMPUTED.csv", index=False)

# parseable = [
#     [str(i).removesuffix("-0700").split("T")[0].split("-"), str(i).removesuffix("-0700").split("T")[1].split(":")] for i
#     in
#     timestamps]
#
# condition = False
# for i in parseable:
#     if i[0] == missingdate and i[1] == [starthour, startmin, startsec]:
#         condition = True
#     if i[0] == missingdate and i[1] == [endhour, endmin, endsec]:
#         condition = False
#     if condition:
#         count = 0
#         sum = 0
#         for date in [["2014", "05", "29"], ["2014", "05", "31"], ["2014", "06", "01"], ["2014", "06", "02"],
#                      ["2014", "06", "03"], ["2014", "06", "04"], ["2014", "06", "05"]]:
#             for z in range(len(parseable)):
#                 if parseable[z] == [date, i[1]]:
#                     sum += anglez[z]
#                     count += 1
#                     break
#         print(sum/count)
#         print(count)
