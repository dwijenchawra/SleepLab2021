import pandas as pd
import rpy2
import os


completedFilesPath = r"C:\Users\Jamie\Documents\biobank_analysis_files\completecsv"
completedFiles = [os.path.join(completedFilesPath, file) for file in os.listdir(completedFilesPath)]

