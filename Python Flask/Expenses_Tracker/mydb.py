# import modules
from tkinter import *
from tkinter import ttk
import datetime as dt  # Fix typo: datatime to datetime
from mydb import Database
from tkinter import messagebox

# object for Database
data = Database(db='myexpense.db')

# global variables
count = 0
selected_rowid = 0

def saveRecord():
    global data
    data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=purchase_date.get())
