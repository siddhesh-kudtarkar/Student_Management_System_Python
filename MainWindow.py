from tkinter import Tk, Button, RAISED, messagebox
import AddWindow

class MainWindow:
    def __init__(self, window):
        self.window = window

        

    def openWindow(self, windowName):
        self.window.deiconify()
        if (windowName == "addWindow"):
            aw = Tk()
            addWindow = AddWindow.AddWindow(aw)
            addWindow.mainloop()

    def exitFunction(self):
        result = messagebox.askyesno("Confirm Exit", "Do you really want to exit?")
        if (result > 0):
            self.window.destroy()

    def deiconify(self):
        self.window.deiconify()

    def withdraw(self):
        self.window.withdraw()
            