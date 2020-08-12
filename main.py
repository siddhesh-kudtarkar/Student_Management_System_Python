from tkinter import Tk, Button, Label, Entry, RAISED, Toplevel, scrolledtext, INSERT, END, WORD, messagebox, Text, PhotoImage
import functions, pickle, os

def openWindow(windowName):
    mainWindow.withdraw()
    if (windowName == "addWindow"):
        addWindow.deiconify()
    elif (windowName == "viewWindow"):
        if (functions.dbCreated):
            viewWindow.deiconify()
            records = functions.getRecords()
            stxtViewData.configure(state="normal")
            stxtViewData.delete('0.0', END)
            for elem in records:
                stxtViewData.insert(INSERT, "".join(["Roll No.: ", str(elem[0])]))
                stxtViewData.insert(INSERT, "".join(["\nName: ", str(elem[1])]))
                stxtViewData.insert(INSERT, "".join(["\nMarks (out of 100): ", str(elem[2]), "\n", ("-" * 45)]))
                stxtViewData.insert(INSERT, "\n\n")
            stxtViewData.configure(state="disabled")
        else:
            mainWindow.deiconify()
            messagebox.showerror("Error", "Database is empty. Enter some data in the database first.")
    elif (windowName == "updateWindow"):
        if (functions.dbCreated):
            updateWindow.deiconify()
        else:
            mainWindow.deiconify()
            messagebox.showerror("Error", "Database is empty. Enter some data in the database first.")
    elif (windowName == "deleteWindow"):
        if (functions.dbCreated):
            deleteWindow.deiconify()
        else:
            mainWindow.deiconify()
            messagebox.showerror("Error", "Database is empty. Enter some data in the database first.")

def backFunction(action):
    mainWindow.deiconify()
    if (action == "backFromAdd"):
        addWindow.withdraw()
    elif (action == "backFromView"):
        viewWindow.withdraw()
    elif (action == "backFromUpdate"):
        updateWindow.withdraw()
    elif (action == "backFromDelete"):
        deleteWindow.withdraw()

#Main Window
mainWindow = Tk()
print("Starting the program...\nFetching some additional details...")
mainWindow.title("Student Management System")
mainWindow.configure(background="Light Blue")
mainWindow.geometry("570x560+400+110")
mainWindow.iconphoto(False, PhotoImage(file="icon.png"))
mainWindow.resizable(0, 0)

btnAdd = Button(mainWindow, text="Add", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=lambda:openWindow("addWindow"))
btnAdd.pack(pady=10)

btnView = Button(mainWindow, text="View", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=lambda:openWindow("viewWindow"))
btnView.pack(pady=10)

btnUpdateAction = Button(mainWindow, text="Update", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=lambda:openWindow("updateWindow"))
btnUpdateAction.pack(pady=10)

btnDelete = Button(mainWindow, text="Delete", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=lambda:openWindow("deleteWindow"))
btnDelete.pack(pady=10)

btnBarChart = Button(mainWindow, text="Bar Chart", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=functions.showBarChart)
btnBarChart.pack(pady=10)

btnExit = Button(mainWindow, text="Exit", width=15, background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), relief=RAISED, command=lambda:functions.exitFunction(mainWindow))
btnExit.pack(pady=10)

txtCityTemp = Text(mainWindow, width=40, height=1, background="Light Yellow", foreground="Black", font=("Calibri", 16, "bold"), wrap=WORD)
txtCityTemp.pack(pady=10)

txtQuoteOfTheDay = Text(mainWindow, width=40, height=5, background="Light Yellow", foreground="Black", font=("Calibri", 16, "bold"), wrap=WORD)
txtQuoteOfTheDay.pack(pady=10)

if (os.path.exists("data.ser")):
    with open("data.ser", "rb") as f:
        functions.dbCreated = pickle.load(f)

city, temp,quote = functions.getCityTempQuote()
txtCityTemp.insert(INSERT, "".join([city, ":\t\t\t\t", str(temp), "\u2103"]))
txtQuoteOfTheDay.insert(INSERT, "".join(["Quote of the day:\n", quote]))
txtCityTemp.configure(state="disabled")
txtQuoteOfTheDay.configure(state="disabled")

print("Program started...")

#Add Window
addWindow = Toplevel(mainWindow)
addWindow.title("Add a Student's Record")
addWindow.configure(background="Light Blue")
addWindow.geometry("450x450+400+150")
addWindow.iconphoto(False, PhotoImage(file="icon.png"))
addWindow.resizable(0, 0)
addWindow.protocol("WM_DELETE_WINDOW", functions.windowCloseAction)

lblAddRollNumber = Label(addWindow, text="Enter the roll number:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblAddRollNumber.pack(pady=10)

entAddRollNumber = Entry(addWindow, font=("Calibri", 16, "bold"), width=24)
entAddRollNumber.pack(pady=10)

lblAddName = Label(addWindow, text="Enter the name:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblAddName.pack(pady=10)

entAddName = Entry(addWindow, font=("Calibri", 16, "bold"), width=24)
entAddName.pack(pady=10)

lblAddMarks = Label(addWindow, text="Enter the marks:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblAddMarks.pack(pady=10)

entAddMarks = Entry(addWindow, font=("Calibri", 16, "bold"), width=24)
entAddMarks.pack(pady=10)

btnAddAction = Button(addWindow, text="Add", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:functions.Validators("add", entAddRollNumber.get(), entAddName.get(), entAddMarks.get()))
btnAddAction.pack(pady=10)

btnAddBack = Button(addWindow, text="Back", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:backFunction("backFromAdd"))
btnAddBack.pack(pady=10)

addWindow.withdraw()

#View Window
viewWindow = Toplevel(mainWindow)
viewWindow.title("View Students' Records")
viewWindow.configure(background="Light Blue")
viewWindow.geometry("450x450+400+150")
viewWindow.resizable(0, 0)
viewWindow.iconphoto(False, PhotoImage(file="icon.png"))
viewWindow.protocol("WM_DELETE_WINDOW", functions.windowCloseAction)

stxtViewData = scrolledtext.ScrolledText(viewWindow, width=45, height=21)
stxtViewData.pack(pady=10)

btnViewBack = Button(viewWindow, text="Back", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:backFunction("backFromView"))
btnViewBack.pack(pady=10)

viewWindow.withdraw()

#Update Window
updateWindow = Toplevel(mainWindow)
updateWindow.title("Update a Student's Record")
updateWindow.configure(background="Light Blue")
updateWindow.geometry("450x450+400+150")
updateWindow.resizable(0, 0)
updateWindow.iconphoto(False, PhotoImage(file="icon.png"))
updateWindow.protocol("WM_DELETE_WINDOW", functions.windowCloseAction)

lblUpdateRollNumber = Label(updateWindow, text="Enter the roll number:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblUpdateRollNumber.pack(pady=10)

entUpdateRollNumber = Entry(updateWindow, font=("Calibri", 16, "bold"), width=24)
entUpdateRollNumber.pack(pady=10)

lblUpdateName = Label(updateWindow, text="Enter the name:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblUpdateName.pack(pady=10)

entUpdateName = Entry(updateWindow, font=("Calibri", 16, "bold"), width=24)
entUpdateName.pack(pady=10)

lblUpdateMarks = Label(updateWindow, text="Enter the marks:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblUpdateMarks.pack(pady=10)

entUpdateMarks = Entry(updateWindow, font=("Calibri", 16, "bold"), width=24)
entUpdateMarks.pack(pady=10)

btnUpdateAction = Button(updateWindow, text="Update", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:functions.Validators("update", entUpdateRollNumber.get(), entUpdateName.get(), entUpdateMarks.get()))
btnUpdateAction.pack(pady=10)

btnUpdateBack = Button(updateWindow, text="Back", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:backFunction("backFromUpdate"))
btnUpdateBack.pack(pady=10)

updateWindow.withdraw()

#Delete Window
deleteWindow = Toplevel(mainWindow)
deleteWindow.title("Delete a Student's Record")
deleteWindow.configure(background="Light Blue")
deleteWindow.geometry("450x450+400+150")
deleteWindow.resizable(0, 0)
deleteWindow.iconphoto(False, PhotoImage(file="icon.png"))
deleteWindow.protocol("WM_DELETE_WINDOW", functions.windowCloseAction)

lblDeleteRollNumber = Label(deleteWindow, text="Enter the roll number:", background="Light Blue", font=("Calibri", 16, "bold"), width=22)
lblDeleteRollNumber.pack(pady=10)

entDeleteRollNumber = Entry(deleteWindow, font=("Calibri", 16, "bold"), width=24)
entDeleteRollNumber.pack(pady=10)

btnDeleteAction = Button(deleteWindow, text="Delete", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:functions.Validators("delete", entDeleteRollNumber.get()))
btnDeleteAction.pack(pady=10)

btnDeleteBack = Button(deleteWindow, text="Back", background="Light Yellow", activebackground="Green", activeforeground="White", font=("Calibri", 16, "bold"), width=22, command=lambda:backFunction("backFromDelete"))
btnDeleteBack.pack(pady=10)

deleteWindow.withdraw()

mainWindow.mainloop()