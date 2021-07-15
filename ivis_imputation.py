import math

import pandas as pd
import os
from tqdm import tqdm
from ggir_csv_prep_for_nparact import convertForNPARact

maskedLocation = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\maskedFiles"


class Masks:
    twelveHourGap = [(22, 10)]
    twoHourGap = [(10, 12), (12, 14), (14, 16), (16, 18), (18, 20)]
    fourHourGap = [(10, 2), (2, 6), (6, 10)]
    sixHourGap = [(10, 4), (4, 10)]
    multipleSingleDay = [((10, 12), (14, 16), (18, 20))]
    multipleInWeek = [((10, 12), (6, 8))]


def applyMask(filePath, mask, weekday, destination):
    # 2014/10/01 10:15:00,23.6104
    df = pd.read_csv(filePath, header=None)
    for maskvalue in mask:
        maskedFileName = os.path.join(maskedLocation, os.path.basename(filePath)[:-4] + f".{}")
        for i in range(0, len(df.iloc[:, 0])):
            time = str(df.iloc[i, 0])
            timeList = [time.split(" ")[0].split("/"), time.split(" ")[1].split(":")]
            if True and timeList[1][0] == str(maskvalue[0]):
                maskDuration = abs(maskvalue[1] - maskvalue[0]) * 720  # hours of time * samples per hour (0.2hz samples = 720 samples per hour)
                df.iloc[i:i + maskDuration, 1] = 0
                df.to_csv(f"{}")


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
    applyMask(filePath, Masks.twelveHourGap, "Wednesday", maskedLocation)
