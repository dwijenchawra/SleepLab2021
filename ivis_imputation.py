import datetime
import math

import pandas as pd
import os

from tqdm import tqdm
from ggir_csv_prep_for_nparact import convertForNPARact

completedFilesPath = r"C:\Users\Jamie\Documents\biobank_analysis_files\completecsv"
maskedLocation = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\maskedFiles"
imputedLocation = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\imputedFiles"
nparACTPreppedFiles = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\nparACTPreppedFiles"


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


def separateTimestamp(time):
    return [time.split(" ")[0].split("-"), time.split(" ")[1].split(":")]


def imputeSingleIntervalMask(maskedFileName, weekday, mask, maskStart, maskDuration):
    imputedFileName = os.path.join(imputedLocation,
                                   os.path.basename(filePath)[:-4] + f".{weekday}.{maskToString(mask)}.IMPUTED.csv")
    df = pd.read_csv(maskedFileName, header=None)
    day = datetime.timedelta(days=1)

    for i in tqdm(range(0, maskDuration)):  # loop over mask
        time = str(df.iloc[maskStart + i, 0])

        sum = 0
        count = 0
        loc = maskStart + (1440 * 12)  # mins per day * samples per min
        while True:
            try:
                sum += float(df.iloc[loc, 1])
                loc += (1440 * 12)
                count += 1
            except IndexError:
                try:
                    avg = sum / count
                except ZeroDivisionError as s:
                    imputedFileName = os.path.join(imputedLocation,
                                                   os.path.basename(filePath)[:-4] + f".{weekday}.{maskToString(mask)}.IMPUTED.ZERODIVBLANK.csv")
                    df.to_csv(imputedFileName, header=None, index=None)
                    return None
                df.iloc[maskStart + i, 1] = avg
                break

    df.to_csv(imputedFileName, header=None, index=None)


def imputeMultipleInDay(maskedFileName, dfToImpute, weekday, mask, maskStart, maskDuration):
    imputedFileName = os.path.join(imputedLocation,
                                   os.path.basename(filePath)[:-4] + f"{weekday}.{maskToString(mask)}.IMPUTED.csv")
    day = datetime.timedelta(days=1)

    # [((10, 12), (14, 16), (18, 20))]
    for maskvalue in mask[0]:
        maskDuration = abs(maskvalue[1] - maskvalue[0]) * 720
        for i in tqdm(range(0, maskDuration)):  # loop over mask
            time = str(dfToImpute.iloc[maskStart + i, 0])

            sum = 0
            count = 0
            loc = maskStart + (1440 * 12)  # mins per day * samples per min
            while True:
                try:
                    sum += float(dfToImpute.iloc[loc, 1])
                    loc += (1440 * 12)
                    count += 1
                except IndexError:
                    try:
                        avg = sum / count
                    except ZeroDivisionError as s:
                        return None
                    dfToImpute.iloc[maskStart + i, 1] = avg
                    break

    # dfToImpute.to_csv(imputedFileName, header=None, index=None)


def applyMaskOnce(filePath, mask, weekday, destination):
    for maskvalue in mask:
        maskedFileName = os.path.join(maskedLocation,
                                      os.path.basename(filePath)[
                                      :-4] + f".{weekday}.{maskToString(maskvalue)}.MASKED.csv")
        df = pd.read_csv(filePath, header=None)
        for i in range(0, len(df.iloc[:, 0])):
            time = str(df.iloc[i, 0])
            timeList = separateTimestamp(time)
            dayString = datetime.date(int(timeList[0][0]), int(timeList[0][1]), int(timeList[0][2])).strftime("%A")
            # print(dayString)
            # print(timeList)
            # print(time)
            if dayString == weekday and timeList[1][0] == str(maskvalue[0]):
                # hours of time * samples per hour (0.2hz samples = 720 samples per hour)
                maskDuration = abs(maskvalue[1] - maskvalue[0]) * 720
                df.iloc[i:i + maskDuration, 1] = 0
                df.to_csv(maskedFileName, header=False, index=False)

                imputeSingleIntervalMask(maskedFileName, weekday, maskvalue, i, maskDuration)

                break


def applyMultipleMaskSingleDay(filePath, mask, weekday, destination):
    # [((10, 12), (14, 16), (18, 20))]
    maskedFileName = os.path.join(maskedLocation,
                                  os.path.basename(filePath)[:-4] + f".{weekday}.{maskToString(mask[0])}.csv")
    df = pd.read_csv(filePath, header=None)
    imputedDF = df.copy(deep=True)

    for maskvalue in mask[0]:
        for i in range(0, len(df.iloc[:, 0])):
            time = str(df.iloc[i, 0])
            timeList = separateTimestamp(time)
            dayString = datetime.date(int(timeList[0][0]), int(timeList[0][1]), int(timeList[0][2])).strftime("%A")
            if dayString == weekday and timeList[1][0] == str(maskvalue[0]):
                # hours of time * samples per hour (0.2hz samples = 720 samples per hour)
                maskDuration = abs(maskvalue[1] - maskvalue[0]) * 720
                df.iloc[i:i + maskDuration, 1] = 0

                imputeMultipleInDay(maskedFileName, imputedDF, mask, weekday, i, imputedLocation)

                break

    df.to_csv(maskedFileName, header=False, index=False)
    imputedDF.to_csv(imputedLocation, header=None, index=None)


# def applyMaskWeek(filePath, multipleInWeek, maskedLocation):


print("Creating completedfiles list")
completedFiles = [os.path.join(completedFilesPath, file) for file in os.listdir(completedFilesPath)]

print("Starting nparACT conversion")
if len(os.listdir(nparACTPreppedFiles)) == 0:
    for filePath in tqdm(completedFiles):
        convertForNPARact(filePath, nparACTPreppedFiles)

# print("Getting IV/IS for complete files")
# for filePath in tqdm(completedFiles):
#     nparACT = importr("nparACT")
#     nparACT_base = nparACT.nparACT_base
#     nparACT_base(filePath, SR = 12/60)

print("Applying selected mask to files and imputing")

nparACTPreppedFilesList = [os.path.join(nparACTPreppedFiles, file) for file in os.listdir(nparACTPreppedFiles)]

count = 1
for filePath in tqdm(nparACTPreppedFilesList):
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
    # applyMultipleMaskSingleDay(filePath, SingleDayMasks.multipleSingleDay, "Wednesday", maskedLocation)
