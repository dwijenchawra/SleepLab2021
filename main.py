import pandas

completefiles = []
df200 = pandas.read_csv("E:\dwije\Documents\part2_summary_200.csv")
df35 = pandas.read_csv("E:\dwije\Documents\part2_summary_35.csv")

validweekdays = df200["N valid WEdays"]
validweekends = df200["N valid WKdays"]
filenames = df200["filename"]

prev = 0
list = []
for i in range(len(filenames)):
    if validweekdays[i] + validweekends[i] == 6:
        completefiles.append(filenames[i])

CSV_PATH = 'F:\\data_output\\output_data\\results\\part2_daysummary.csv'
CWA_FILES_PATH = "F:\\data"
df = pandas.read_csv(CSV_PATH)

print(completefiles)
print(len(completefiles))
