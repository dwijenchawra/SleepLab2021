import datetime
import math

import pandas as pd
import os
from tqdm import tqdm
from ggir_csv_prep_for_nparact import convertForNPARact

maskedLocation = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\maskedFiles"
imputedLocation = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\imputedFiles"


class SingleDayMasks:
    twelveHourGap = [(22, 10)]
    twoHourGap = [(10, 12), (12, 14), (14, 16), (16, 18), (18, 20)]
    fourHourGap = [(10, 2), (2, 6), (6, 10)]
    sixHourGap = [(10, 4), (4, 10)]
    twentyFourHourGap = [(10, 22)]
    multipleSingleDay = [((10, 12), (14, 16), (18, 20))]


class MultipleDayMasks:
    multipleInWeek = [((10, 12), (6, 8))]


def maskToString(maskvalue):
    if type(maskvalue[0]) == int:
        lst = []
        for i in maskvalue:
            lst.append(str(i))
        return "-".join(lst)
    lst = []
    for i in maskvalue:
        if type(i) == tuple:
            lst.append(maskToString(i))
    return ".".join(lst)


def imputeSingleIntervalMask(maskedFileName, maskStart, maskDuration):
    df = pd.read_csv(maskedFileName, header=None)

    week = datetime.timedelta(days=7)

    for i in range(0, len(df.iloc[maskStart:maskStart + maskDuration, 0])): #loop over mask
        time = str(df.iloc[i, 0])
        timestamp = datetime.date.fromisoformat(time)
        df = df.set_index(0)

        while True:
            try:
                timestamp += week


                df.loc()



def separateTimestamp(time):
    return [time.split(" ")[0].split("-"), time.split(" ")[1].split(":")]

# def timeToNPARACTFormat(year, month, day, hour, minute, second):
#     return f"{year}/{month}/{day} {hour}:{minute}:{second}"

def timeToISOFormat(year, month, day, hour, minute, second):
    return f"{year}-{month}-{day} {hour}:{minute}:{second}"


def applyMaskOnce(filePath, mask, weekday, destination):
    for maskvalue in mask:
        if type(maskvalue[0]) == int:
            maskedFileName = os.path.join(maskedLocation,
                                          os.path.basename(filePath)[:-4] + f".{weekday}.{maskToString(maskvalue)}.csv")
            df = pd.read_csv(filePath, header=None)
            for i in range(0, len(df.iloc[:, 0])):
                time = str(df.iloc[i, 0])
                timeList = separateTimestamp(time)
                dayString = datetime.date(int(timeList[0][2]), int(timeList[0][1]), int(timeList[0][2])).strftime("%A")
                if dayString == weekday and timeList[1][0] == str(maskvalue[0]):
                    # hours of time * samples per hour (0.2hz samples = 720 samples per hour)
                    maskDuration = abs(maskvalue[1] - maskvalue[0]) * 720
                    df.iloc[i:i + maskDuration, 1] = 0
                    df.to_csv(maskedFileName, header=False, index=False)

                    imputeSingleIntervalMask(maskedFileName, i, maskDuration)

                    break
        else:
            pass
            # todo implement multiple masks in one day
            # todo implement imputation in one day


# def applyMaskWeek(filePath, multipleInWeek, maskedLocation):


print("Creating completedfiles list")
completedFilesPath = r"C:\Users\Jamie\Documents\biobank_analysis_files\completecsv"
completedFiles = [os.path.join(completedFilesPath, file) for file in os.listdir(completedFilesPath)]

print("Starting nparACT conversion")
if len(os.listdir(r'C:\Users\Jamie\Documents\biobank_analysis_files\completenparactcsv')) == 0:
    for filePath in tqdm(completedFiles):
        convertForNPARact(filePath, r'C:\Users\Jamie\Documents\biobank_analysis_files\completenparactcsv')

# print("Getting IV/IS for complete files")
# for filePath in tqdm(completedFiles):
#     nparACT = importr("nparACT")
#     nparACT_base = nparACT.nparACT_base
#     nparACT_base(filePath, SR = 12/60)

print("Applying selected mask to files and imputing")

nparACTCSVPath = r"C:\Users\Jamie\Documents\biobank_analysis_files\completenparactcsv"
completedNparACTFiles = [os.path.join(nparACTCSVPath, file) for file in os.listdir(nparACTCSVPath)]

for filePath in tqdm(completedNparACTFiles):
    applyMaskOnce(filePath, SingleDayMasks.twelveHourGap, "Wednesday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.twelveHourGap, "Saturday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.twoHourGap, "Wednesday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.twoHourGap, "Saturday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.fourHourGap, "Wednesday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.fourHourGap, "Saturday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.sixHourGap, "Wednesday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.sixHourGap, "Saturday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.twentyFourHourGap, "Wednesday", maskedLocation)
    applyMaskOnce(filePath, SingleDayMasks.twentyFourHourGap, "Saturday", maskedLocation)
    # applyMaskOnce(filePath, SingleDayMasks.multipleSingleDay, "Wednesday", maskedLocation)
    # applyMaskOnce(filePath, SingleDayMasks.multipleSingleDay, "Saturday", maskedLocation)

    # applyMaskWeek(filePath, MultipleDayMasks.multipleInWeek, maskedLocation)
