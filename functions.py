from tkinter import messagebox
from mysql.connector import connect, DatabaseError
import re, socket, requests, bs4, pickle
import matplotlib.pyplot as plt

dbCreated = False

def exitFunction(mainWindow):
    result = messagebox.askyesno("Confirm Exit", "Do you really want to exit?")
    if (result > 0):
        mainWindow.destroy()

def windowCloseAction():
    messagebox.showinfo("Notification", "Click on Back button to go to the main window.")

def dbConnection(userName, passWord, hostName):
    conn = None
    try:
        conn = connect(
            user = userName,
            passwd = passWord,
            host = hostName
        )
    except DatabaseError as de:
        messagebox.showerror("Database Error", de)
    except Exception as e:
        messagebox.showerror("Error", e)
    finally:
        return conn

def getRecords():
    try:
        conn = dbConnection("root", "", "localhost")
        cur = conn.cursor()
        cur.execute("USE Student")
        cur.execute("SELECT * FROM student")
        result = cur.fetchall()
        conn.commit()
    except DatabaseError as de:
        conn.rollback()
        messagebox.showerror("Database Error", de)
    except Exception as e:
        messagebox.showerror("Error", e)
    finally:
        if (conn != None):
            conn.close()
    return result

def showBarChart():
    if (dbCreated):
        names, marks, conn = [], [], None
        try:
            conn = dbConnection("root", "", "localhost")
            cur = conn.cursor()
            cur.execute("USE Student")
            cur.execute("SELECT * FROM student")
            records = cur.fetchall()
            for elem in records:
                names.append(elem[1])
                marks.append(elem[2])
            conn.commit()
            plt.bar(names, marks, width=0.5)
            plt.title("Marks of Students")
            plt.xlabel("Student Names")
            plt.ylabel("Marks")
            plt.show()
        except DatabaseError as de:
            conn.rollback()
            messagebox.showerror("Database Error", de)
        except Exception as e:
            messagebox.showerror("Error", e)
        finally:
            if (conn != None):
                conn.close()
    else:
        messagebox.showerror("Error", "Database is empty. Enter some data in the database first.")

def getCityTempQuote():
    city, temp, quote = "", "", ""
    try:
        socket.create_connection(("www.google.com", 80))
        result = requests.get("https://www.ipinfo.io")
        data = result.json()
        city = data["city"]
        addr1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
        addr2 = "".join(["&q=", city])
        addr3 = "&appid=c6e315d09197cec231495138183954bd"
        apiAddress = "".join([addr1, addr2, addr3])
        result = requests.get(apiAddress)
        data = result.json()
        temp = data["main"]["temp"]
        result = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
        soup = bs4.BeautifulSoup(result.text, "lxml")
        quote = soup.find("img", {"class": "p-qotd"})
        quote = quote["alt"]
    except OSError as oe:
        messagebox.showerror("Error", oe)
    except Exception as e:
        messagebox.showerror("Error", e)
    finally:
        return city, temp, quote

class Student:
    def __init__(self, rollNumber, name="", marks=0):
        self.rollNumber = rollNumber
        self.name = name
        self.marks = marks

    def addRecord(self):
        try:
            global dbCreated
            conn = dbConnection("root", "", "localhost")
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS Student")
            cur.execute("USE Student")
            cur.execute("CREATE TABLE IF NOT EXISTS student(roll_number INT PRIMARY KEY NOT NULL, name VARCHAR(25) NOT NULL, marks INT NOT NULL)")
            cur.execute("INSERT INTO student VALUES(%s, '%s', %s)" %(self.rollNumber, self.name, self.marks))
            conn.commit()
            dbCreated = True
            with open("data.ser", "wb") as f:
                pickle.dump(dbCreated, f)
            messagebox.showinfo("Record inserted", "1 record inserted.")
        except DatabaseError as de:
            conn.rollback()
            messagebox.showerror("Database Error", de)
        except Exception as e:
            messagebox.showerror("Error", e)
        finally:
            if (conn != None):
                conn.close()

    def updateRecord(self):
        try:
            conn = dbConnection("root", "", "localhost")
            cur = conn.cursor()
            cur.execute("USE Student")
            cur.execute("UPDATE student SET name='%s', marks=%s WHERE roll_number=%s" %(self.name, self.marks, self.rollNumber))
            conn.commit()
            messagebox.showinfo("Record updated", "".join(["Record of Roll No. ", str(self.rollNumber), " updated."]))
        except DatabaseError as de:
            conn.rollback()
            messagebox.showerror("Database Error", de)
        except Exception as e:
            messagebox.showerror("Error", e)
        finally:
            if (conn != None):
                conn.close()

    def deleteRecord(self):
        try:
            conn = dbConnection("root", "", "localhost")
            cur = conn.cursor()
            cur.execute("USE Student")
            records, valueFound = getRecords(), False
            for elem in records:
                if (self.rollNumber == elem[0]):
                    cur.execute("DELETE FROM student WHERE roll_number=%s" %(self.rollNumber, ))
                    conn.commit()
                    valueFound = True
                    messagebox.showinfo("Record deleted", "".join(["Record of Roll No. ", str(self.rollNumber), " deleted."]))
            if not valueFound:
                raise Exception("".join(["Record of Roll No. ", str(self.rollNumber), " not found."]))
        except DatabaseError as de:
            conn.rollback()
            messagebox.showerror("Database Error", de)
        except Exception as e:
            messagebox.showerror("Error", e)
        finally:
            if (conn != None):
                conn.close()

class Validators:
    def __init__(self, action, rollNumber, name="", marks=0):
        self.rollNumber = 0
        self.name = ""
        self.marks = 0

        if ((action == "add") or (action == "update")):
            if (self.rollNumberValidator(rollNumber)):
                if (self.nameValidator(name)):
                    if(self.marksValidator(marks)):
                        if (action == "update"):
                            s = Student(self.rollNumber, self.name, self.marks)
                            s.updateRecord()
                        elif (action == "add"):
                            s = Student(self.rollNumber, self.name, self.marks)
                            s.addRecord()
        elif (action == "delete"):
            if (self.rollNumberValidator(rollNumber)):
                s = Student(self.rollNumber)
                s.deleteRecord()

    def rollNumberValidator(self, rollNumber):
        rollNumber = rollNumber.strip()
        result = False
        if (rollNumber != ""):
            if (re.compile("^[0-9]+$").match(rollNumber)):
                rollNumber = int(rollNumber)
                if (rollNumber > 0):
                    self.rollNumber = rollNumber
                    result = True
                else:
                    messagebox.showerror("Invalid Roll Number", "Roll Number should consist of positive and non-zero integers only.")
            else:
                messagebox.showerror("Invalid Roll Number", "Roll Number should consist of positive and non-zero integers only.")
        else:
            messagebox.showerror("Invalid Roll Number", "Roll Number field should not be kept empty.")
        return result

    def nameValidator(self, name):
        name = name.strip()
        result = False
        if (name != ""):
            if (re.compile("^[a-zA-Z]+$").match(name)):
                if ((len(name) >= 2) and (len(name) <= 25)):
                    self.name = name
                    result = True
                else:
                    messagebox.showerror("Invalid Name", "Minimum length of name should be 2 letters and maximum length is 25 letters.")
            else:
                messagebox.showerror("Invalid Name", "Name should consist of alphabets only.")
        else:
            messagebox.showerror("Invalid Name", "Name field should not be kept empty.")
        return result

    def marksValidator(self, marks):
        marks = marks.strip()
        result = False
        if (marks != ""):
            if (re.compile("^[0-9]+$").match(marks)):
                marks = int(marks)
                if ((marks >= 0) and (marks <= 100)):
                    self.marks = marks
                    result = True
                else:
                    messagebox.showerror("Invalid Marks", "Marks should consist of positive integers only and must be in the range of 0-100.")
            else:
                messagebox.showerror("Invalid Marks", "Marks should consist of positive integers only and must be in the range of 0-100.")
        else:
            messagebox.showerror("Invalid Marks", "Marks field should not be kept empty.")
        return result