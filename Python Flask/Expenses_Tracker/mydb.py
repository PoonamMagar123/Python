# import modules 
from tkinter import *
from tkinter import ttk
import datetime as dt
from main import *
from tkinter import messagebox


# object for Database
data = Database(db='myexpense.db')

# global variables
count = 0
selected_rowid = 0

def saveRecord():
    global data
    data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=purchase_date.get())

def setData():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearEntries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transction_date.delete(0, 'end')

def fetch_records():
    f = data.fetchRecord('select rowid, * from expense_record')
    global count
    for rec in f:
        tv.insert(parent='',index='0', iid=count, values=(rec[0],rec[1], rec[2], rec[3]))
        count +=1 
        tv.after(400, refreshData)

def select_record(event):
    global selected_rowid
    selected = tv.focus()
    val = tv.item(selected, 'values')

    try:
        selected_rowid = val[0]
        d = val[3]
        namevar.set(val[1])
        amtvar.set(val[2])
        dopvar.set(val[d])
    except Exception as ep:
        pass

# create tkinter obkect
ws = Tk()
ws.title('Daily Expenses')
