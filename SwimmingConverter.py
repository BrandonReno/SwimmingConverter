from tkinter import *
from tkinter.ttk import Combobox
from KNN import KNN

class ConversionUI:
    def __init__(self):
        self. window = Tk()
        self.StrokeEvents = ["Backstroke", "Breaststroke", "Butterfly", "Freestyle", "IndividualMedley"]
        self.window.title("Swimming Time Converter With KNN")
        self.window.geometry("600x400+10+20")
        self.Distance = IntVar()
        self.Time = IntVar()
        self.Sec = IntVar()
        self.Min = IntVar()
        self.Mili = IntVar()
        self.Stroke = StringVar()
        self.Gender = StringVar()
        self.t = Entry(self.window, textvariable = self.Min,width=4)
        self.t2 = Entry(self.window, textvariable = self.Sec,width=4)
        self.t3 = Entry(self.window, textvariable = self.Mili, width= 4)
        
    def BuildLabels(self):
        lbl=Label(self.window, text="Swimming Time Conversion Tool", fg='red', font=("Helvetica", 20))
        lbl.place(x=110, y=40)

    def BuildRadioButtons(self):
        r1=Radiobutton(self.window, text="Male", variable=self.Gender,value="Male")
        r2=Radiobutton(self.window, text="Female", variable=self.Gender,value="Female")
        r1.place(x=50,y=110)
        r2.place(x=50, y=140)
        r1=Radiobutton(self.window, text="50", variable=self.Distance,value= 50)
        r2=Radiobutton(self.window, text="100", variable=self.Distance,value=100)
        r3=Radiobutton(self.window, text="200", variable=self.Distance,value=200)
        r4=Radiobutton(self.window, text="400", variable=self.Distance,value=400)
        r1.place(x=50,y=210)
        r2.place(x=50, y=240)
        r3.place(x=50, y=270)
        r4.place(x=50, y=300)

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg, font="Helvectiva")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def BuildComboBox(self):
        cb=Combobox(self.window, values=self.StrokeEvents, textvariable=self.Stroke)
        cb.place(x=130, y=210)

    def BuildTextInput(self):
        self.t.place(x=130,y=270)
        self.t2.place(x=170, y=270)
        self.t3.place(x=210, y=270)

    def BuildButtons(self):
        bt = Button(self.window, text = "Calculate Conversion", command= self.display)
        bt.place(x=300,y=300)

    def getTime(self):
        Time = str(self.t.get()) + str(self.t2.get()) + str(self.t3.get())
        self.Time = int(Time)
        return self.Time

    def display(self):
        k = KNN(self.getDataset(), self.getTime())
        time = k.main()
        x = Label(self.window, text = time, font = ("Helvectiva", 20))
        x.place(x=110, y=80)

    def getDataset(self):
            if self.Gender.get() == "Male":
                for strokeEV in self.StrokeEvents:
                    if self.Stroke.get() == strokeEV:
                        Dataset = (str(self.Distance.get()) + self.Stroke.get() + "Data")
            else:
                for strokeEV in self.StrokeEvents:
                    if self.Stroke.get() == strokeEV:
                        Dataset = "f" +(str(self.Distance.get()) + self.Stroke.get() + "Data")
            return Dataset


    def main(self):
        self.BuildLabels()
        self.BuildRadioButtons()
        self.BuildComboBox()
        self.BuildButtons()
        self.BuildTextInput()
        self.window.mainloop()

if __name__ == "__main__":
    s = ConversionUI()
    s.main()



