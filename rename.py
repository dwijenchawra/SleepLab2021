import os
import shutil

for i in [os.path.join(r"/imputedFiles", file) for file in os.listdir(r"/imputedFiles")]:
    ind = i.find("RData") + 5
    newstr = f"{i[0:ind]}.{i[ind:]}"
    shutil.move(i, newstr)