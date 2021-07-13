import time

import pandas as pd
import rpy2
import os
from rpy2.robjects.packages import importr

from tqdm import tqdm

from ggir_csv_prep_for_nparact import convertForNPARact

completedFilesPath = r"C:\Users\Jamie\Documents\biobank_analysis_files\completecsv"
completedFiles = [os.path.join(completedFilesPath, file) for file in os.listdir(completedFilesPath)]

print("Starting NPARact conversion")
for filePath in tqdm(completedFiles):
    convertForNPARact(filePath, r'C:\Users\Jamie\Documents\biobank_analysis_files\completenparactcsv')



