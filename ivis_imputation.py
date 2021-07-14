import pandas as pd
import os
from tqdm import tqdm
from ggir_csv_prep_for_nparact import convertForNPARact


# import rpy2
# from rpy2.robjects.packages import importr

class Masks:
    twelveHourGap = [(22, 10)]
    twoHourGap = [(10, 12), (12, 14), (14, 16), (16, 18), (18, 20)]
    fourHourGap = [(10, 2), (2, 6), (6, 10)]
    sixHourGap = [(10, 4), (4, 10)]
    multipleSingleDay = [(10, 12), (14, 16), (18, 20)]
    multipleInWeek = [(10, 12), (6, 8)]


def applyMask(filePath, mask):
    df = pd.read_csv(filePath)


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

print("Applying selected mask to files")

for filePath in tqdm(completedFiles):
    applyMask(filePath, Masks.twelveHourGap)
