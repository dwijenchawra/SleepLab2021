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
    initialtime = parseable[i][1]


df.to_csv("F:\\ggir_missing_test\\out\\output_data\\meta\\csv\\1001787_90001_0_0.cwa.RData.IMPUTED.csv", index=False)
