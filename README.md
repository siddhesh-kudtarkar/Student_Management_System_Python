# Project Title: 

Student Management System.

# Getting Started: 

Setting up and installing this software is easy by just installing Python3, Python3's Tkinter GUI library, and some Python3 modules.

# Prerequisites:

**Softwares needed:**
1.	Python3.
2.	Python3's Tkinter GUI library.
3.	MySQL.
4.	Python3 modules: mysql-connector, requests, matplotlib, bs4.

**Installation links of the required softwares:**
1.	Python3: <https://www.python.org/downloads/>
2.	MySQL: <https://dev.mysql.com/downloads/>

# Installing required softwares:

**For Windows users:**
1.	Download Python3 from the above given link and install it. When installing Python3, make sure that under Tcl/Tk you select Will be installed on hard drive. The option 'Tcl/Tk' must be checked to allow Python installer to install Python's Tkinter GUI library.
2.	Download MySQL from the official website given above and install it.
3.	Open your command prompt and run the following command to install all the required Python3 modules:

        pip install mysql-connector requests matplotlib bs4

**For Ubuntu/Debian users:**
1.	Install Python3 by running the following command in terminal: sudo apt-get install python3. By default, Debian, Ubuntu or any other Linux distributions come with Python pre-installed.
2.	To install Python3's Tkinter GUI library and Python Package Installer (pip), run the following command in the terminal: 
      
        sudo apt-get install python3-tk tk-dev python3-pip
3.	To install MySQL, run the following command in the terminal:

        sudo apt-get install mysql-server
4.	Finally, run the following command in the terminal to install all the required Python3 modules:

        pip3 install mysql-connector requests matplotlib bs4

**Following the above installation steps for required softwares will set up an environment to run the Student Management System without any hassles.**

# Running the software:

**For Windows users:**
1.  First setup your MySQL credentials in the 'functions.py' file.
2.  Open your command prompt and navigate to the project's directory and run the following command:

        python main.py

**For Ubuntu/Debian users:**
1.  First setup your MySQL credentials in the 'functions.py' file.
2.  Open your terminal and navigate to the project's directory and run the following command:

        python main.py

# Built with:
1.    Python3 - GUI for the software.
2.    MySQL - Database Management System.

# Author:

    Siddhesh Kudtarkar
