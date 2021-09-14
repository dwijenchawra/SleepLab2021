import pandas as pd

imputed = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_imputed\ukbb_imputed IVIS_data_imputed.csv"
# imputed = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_masked\ukbb_masked IVIS_data_masked.csv"

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
    mask = list(map(int, broken[2].split("-")))
    print(mask)
    if broken[-2] == "ZERODIVBLANK":
        masklencol.append(0)
    else:
        masklencol.append(abs(mask[1] - mask[0]))
    # masklencol.append(broken[1])

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
# imputedcsv["Weekday"] = masklencol
imputedcsv.to_csv(imputed, index=None)