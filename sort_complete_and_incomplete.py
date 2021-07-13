import os
import shutil

csv1 = os.listdir(r"C:\Users\Jamie\Documents\biobank_analysis_files\data_output_run1\output_data\meta\csv")
csv2 = os.listdir(r"C:\Users\Jamie\Documents\biobank_analysis_files\data_output_run2\output_data\meta\csv")

completed_cwa = os.listdir(r"C:\Users\Jamie\Documents\biobank_analysis_files\completefiles")
incomplete_cwa = os.listdir(r"C:\Users\Jamie\Documents\biobank_analysis_files\incompletefiles")


for i in csv2:
    print(i.removesuffix(".RData.csv"))
    print(i.removesuffix(".RData.csv") in completed_cwa or i.removesuffix(".RData.csv") in incomplete_cwa)
    if i.removesuffix(".RData.csv") in completed_cwa:
        shutil.copyfile(
            r"C:\Users\Jamie\Documents\biobank_analysis_files\data_output_run2\output_data\meta\csv" + "\\" + i,
            r"C:\Users\Jamie\Documents\biobank_analysis_files\completecsv\\" + i)
    if i.removesuffix(".RData.csv") in incomplete_cwa:
        shutil.copyfile(
            r"C:\Users\Jamie\Documents\biobank_analysis_files\data_output_run2\output_data\meta\csv" + "\\" + i,
            r"C:\Users\Jamie\Documents\biobank_analysis_files\incompletecsv\\" + i)
