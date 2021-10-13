import pandas as pd
from tqdm import tqdm

# imputed = r"C:\Users\Zeitzer Lab\Desktop\DWIJEN_FILES\PycharmProjects\SleepLab2021\ukbb_imputed\ukbb_imputed IVIS_data_imputed.csv"
imputed = r"C:\Users\dwije\PycharmProjects\GGIRanalysis\ukbb_imputed\backup_ukbb_imputed IVIS_data_imputed.csv"

# maskedcsv = pd.read_csv(masked)
imputedcsv = pd.read_csv(imputed)

masklencol = []
weekcol = []

'''
nparactformat_1001778_90001_0_0.cwa.RData.Wednesday.18-20.IMPUTED.ZERODIVBLANK.csv
nparactformat_1001699_90001_0_0.cwa.RData.Saturday.10-12.IMPUTED.csv
nparactformat_1011323_90001_3_0-timeSeries.WEEK.10-12.IMPUTED.csv
'''


def multitester(inputlist):
    try:
        mask = inputlist[3].split("-")
        integer = int(mask[0])
        return True
    except ValueError:
        return False


for row in tqdm(range(len(imputedcsv["filename"]))):
    filename = str(imputedcsv["filename"][row])
    broken = filename.split(".")
    mask = list(map(int, broken[2].split("-")))
    print(mask)
    if broken[-2] == "ZERODIVBLANK":
        masklencol.append("ZERODIVBLANK")
        weekcol.append(broken[1])
    elif multitester(broken):
        masklencol.append(str("MULT" + broken[2]))
        weekcol.append(broken[1])
    else:
        masklencol.append(broken[2])
        weekcol.append(broken[1])
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
imputedcsv["Weekday"] = weekcol
imputedcsv.to_csv(imputed, index=None)