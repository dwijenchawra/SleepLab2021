import pandas as pd

masked = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\old_runs\maskedFiles\Weekly_IVIS_Data_masked.csv"
imputed = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\imputedFiles\Weekly_IVIS_Data_imputed.csv"

maskedcsv = pd.read_csv(masked)
imputedcsv = pd.read_csv(imputed)

isdiff = []
ivdiff = []
# print(imputedcsv)
# print(maskedcsv)

for i in range(len(maskedcsv["IS"])):
    isdiff.append(maskedcsv["IS"][i] - imputedcsv["IS"][i])
    ivdiff.append(maskedcsv["IV"][i] - imputedcsv["IV"][i])

print('\n'.join(map(str, isdiff)))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print('\n'.join(map(str, ivdiff)))
