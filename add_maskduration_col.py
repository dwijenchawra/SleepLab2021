import pandas as pd

# masked = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\maskedFiles\IVIS_Data_masked.csv"
imputed = r"C:\Users\Jamie\PycharmProjects\SleepLab2021\imputedFiles\IVIS_Data_imputed.csv"

# maskedcsv = pd.read_csv(masked)
imputedcsv = pd.read_csv(imputed)

masklencol = []


'''
nparactformat_1001778_90001_0_0.cwa.RData.Wednesday.18-20.IMPUTED.ZERODIVBLANK.csv
nparactformat_1001699_90001_0_0.cwa.RData.Saturday.10-12.IMPUTED.csv
'''
for row in range(len(imputedcsv["filename"])):
    filename = str(imputedcsv["filename"][row])
    broken = filename.split(".")
    mask = list(map(int, broken[4].split("-")))
    print(mask)

    if mask[0] == 22:
        masklencol.append(12)
    else:
        masklencol.append(mask[1] - mask[0])

print(masklencol)
#
# for row in range(len(maskedcsv["filename"])):
#     filename = str(maskedcsv["filename"][row])
#     broken = filename.split(".")
#     mask = list(map(int, broken[4].split("-")))
#     print(mask)
#
#     if mask[0] == 22:
#         masklencol.append(12)
#     else:
#         masklencol.append(mask[1] - mask[0])
#
print(masklencol)
print(len(masklencol))

imputedcsv["Mask Length"] = masklencol
imputedcsv.to_csv(imputed, index=None)