from PandasTest import Data

class FileReader:
    def __init__(self, filename):
        self.data = Data(filename)
        self.Temp = self.data.getData()
        self.SCY = []
        self.LCM = []
        self.Data = []
        self.filename = filename
        self.setUpFile()

    def setUpFile(self):
        for i in range(len(self.Temp)):
            Seperated = self.Temp[i]
            for i in range(0,2):
                individualTime = str(Seperated[i])
                if i == 0:
                    SCYtime = int(individualTime.replace(".", "").replace(":", "").replace("r", ""))
                else:
                    LCMtime = int(individualTime.replace(":", "").replace(".", "").replace("r", ""))
            self.Data.append([SCYtime, LCMtime])

    def getData(self):
        return self.Data


if __name__ == "__main__":
    f = FileReader("200FrData")
    print(f.getData())
        













