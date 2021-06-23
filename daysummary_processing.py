import pandas

completefiles = []

CSV_PATH = 'F:\\data_output_2\\output_data\\results\\part2_daysummary.csv'
CWA_FILES_PATH = "F:\\data"
df = pandas.read_csv(CSV_PATH)

hourscol = df["N valid hours"]
filenames = df["filename"]

prev = 0
list = []
for i in range(len(hourscol)):
    if hourscol[i] != 0:
        list.append(hourscol[i])
    if (prev > 0 and hourscol[i] == 0):
        cond = True
        for z in list:
            if len(list) != 6:
                cond = False
                break
            if z != 24:
                cond = False
                break
        if cond:
            completefiles.append(filenames[i])
        list = []
    prev = hourscol[i]

CSV_PATH = 'F:\\data_output\\output_data\\results\\part2_daysummary.csv'
CWA_FILES_PATH = "F:\\data"
df = pandas.read_csv(CSV_PATH)

hourscol = df["N valid hours"]
filenames = df["filename"]

prev = 0
list = []
for i in range(len(hourscol)):
    if hourscol[i] != 0:
        list.append(hourscol[i])
    if (prev > 0 and hourscol[i] == 0):
        cond = True
        for z in list:
            if len(list) != 6:
                cond = False
                break
            if z != 24:
                cond = False
                break
        if cond:
            completefiles.append(filenames[i])
        list = []
    prev = hourscol[i]

print(completefiles)
print(len(completefiles))

df200 = pandas.read_csv("E:\dwije\Documents\part2_summary_200.csv")
df35 = pandas.read_csv("E:\dwije\Documents\part2_summary_35.csv")
ivtotal = []
istotal = []
filenames200 = df200["filename"].tolist()
filenames35 = df35["filename"].tolist()
iv200 = df200["L5hr_ENMO_mg_0-24h_fullRecording"].tolist()
iv35 = df35["L5hr_ENMO_mg_0-24h_fullRecording"].tolist()
is200 = df200["M10hr_ENMO_mg_0-24h_fullRecording"].tolist()
is35 = df35["M10hr_ENMO_mg_0-24h_fullRecording"].tolist()

print(completefiles)
print(filenames35)

for i in completefiles:
    if i not in filenames200:
        index = filenames200.index(i)
        ivtotal.append(float(iv200[index]))
        istotal.append(float(is200[index]))
    if i not in filenames35:
        index = filenames35.index(i)
        ivtotal.append(float(iv35[index]))
        istotal.append(float(is35[index]))

print("ivtotal")
for i in ivtotal:
    print(i)
print("istotal")
for i in istotal:
    print(i)
