import pickle
class Data:
    def __init__(self,file):
        self.file = file
    def getData(self):
        with open (self.file, "rb") as f:
            x = pickle.load(f)
        return x
            



