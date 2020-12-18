import pandas as pd 
import pickle

class DataFrames:
    def __init__(self):
        self.LCMData = pd.read_csv("FemaleCSV\Top Times Rankings 400 IM LCM.csv")
        self.SCYData = pd.read_csv("FemaleCSV\Top Times Rankings 400 IM SCY.csv")
        self.BothDataArr = [self.LCMData, self.SCYData]
        self.CompletedList = []
    def CreateList(self):
        for ind, row in self.SCYData.iterrows():
            CurrName = row["Full Name"]
            SCYTime = row["Time"]
            for ind, row in self.LCMData.iterrows():
                if row["Full Name"] == CurrName:
                    self.CompletedList.append([SCYTime, row["Time"]])
    def WriteData(self, Name):
        with open (Name, "wb+") as f:
            pickle.dump(self.CompletedList, f)

    def run(self, Name):
        self.CreateList()
        self.WriteData(Name)

if __name__ == "__main__":
    x = DataFrames()
    x.run("F400IndividualMedleyData")
