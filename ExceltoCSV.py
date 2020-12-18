import pandas as pd
import os


directory = 'FemaleExcelTimes'
allFiles = []


for filename in os.listdir(directory):
    dire = directory + "\\" + filename
    direOut = "FemaleCSV" + "\\" + filename + ".csv"
    read_file = pd.read_excel (dire)
    csvf = read_file.to_csv (direOut)
    allFiles.append(csvf)

for c in allFiles:
    filr = pd.read_csv(c)
    filr.drop([])

print(allFiles)
