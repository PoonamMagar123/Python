# import modules 
from tkinter import *
from tkinter import ttk
import datetime as dt
from mydb import *
from tkinter import messagebox

# object for Database
data = Database(db='myexpense.db')

# global variables
count = 0
selected_rowid = 0

def saveRecord():
    global data
    data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())
    fetch_records()
    messagebox.showinfo("Success", f"saved successfully...!")
    clearEntries()
    
def setDate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearEntries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transaction_date.delete(0, 'end')

def fetch_records():
    f = data.fetchRecord('select rowid, * from expense_record')

    global count
    # Clear existing data in the Treeview
    tv.delete(*tv.get_children())
    for rec in f:
        tv.insert(parent='', index='end', iid=count, values=(rec[0], rec[1], rec[2], rec[3]))
        count += 1

def select_record(event):
    global selected_rowid
    selected = tv.focus()
    val = tv.item(selected, 'values')

    try:
        selected_rowid = val[0]
        namevar.set(val[1])
        amtvar.set(val[2])
        dopvar.set(val[3])
    except Exception as ep:
        pass

def update_record():
    global selected_rowid

    selected = tv.focus()
    # update records
    try:
        # Get the current values in the selected row
        current_values = tv.item(selected, 'values')

        # Update records, including the ID (assuming ID is the first column)
        data.updateRecord(namevar.get(), amtvar.get(), dopvar.get(), selected_rowid)

        # Construct the new values tuple with the updated values
        updated_values = (selected_rowid, namevar.get(), amtvar.get(), dopvar.get())

        # Update the grid with the new values
        tv.item(selected, values=updated_values)

        # Fetch and refresh the data
        fetch_records()
        messagebox.showinfo("Success", f"Updated successfully...!")
        clearEntries()

    except Exception as ep:
        messagebox.showerror('Error', ep)

def totalBalance():
    f = data.fetchRecord(query="Select sum(item_price) from expense_record")
    for i in f:
        for j in i:
            messagebox.showinfo('Current Balance: ', f"Total Expense: ' {j}\n Balance Remaining: {5000 - j}")

def refreshData():
    for item in tv.get_children():
        tv.delete(item)
    fetch_records()

# def refreshData():
#     tv.delete(*tv.get_children())
#     fetch_records()

def deleteRow():
    global selected_rowid
    data.removeRecord(selected_rowid)
    refreshData()

# create tkinter object
ws = Tk()
ws.title('Daily Expenses')
# ws.geometry('600*400')

#4 global variables
# variables
f = ('Times new roman', 14)
namevar = StringVar()
amtvar = IntVar()
dopvar = StringVar()

#5 frame widgets
f2 = Frame(ws)
f2.pack() 

f1 = Frame(
    ws,
    padx=10,
    pady=10,
)

f1.pack(expand=True, fill=BOTH)

#6 Label Widget
Label(f1, text='ITEM NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=f).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=f).grid(row=2, column=0, sticky=W)

#7 Entry Widgets 
item_name = Entry(f1, font=f, textvariable=namevar)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)

# Entry grid placement
item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))

# action buttons
cur_date = Button(
    f1,
    text='Current Date',
    font=f,
    bg = '#00B5E1',
    command = setDate,
    width = 15
)

submit_btn = Button(
    f1,
    text='Save Record',
    font=f,
    bg = '#405B2A',
    fg = "white",
    command = saveRecord,
    width = 15
)

clr_btn = Button(
    f1,
    text='Clear Entry',
    font=f,
    bg = '#E3AE2B',
    fg = "white",
    command = clearEntries
)

quit_btn = Button(
    f1,
    text='Exit',
    font=f,
    bg = '#E44331',
    fg = "white",
    command = lambda:ws.destroy()
)

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    bg = '#436573',
    fg = "white",
    command = totalBalance
)

update_btn = Button(
    f1,
    text='Update',
    bg = '#00887A',
    fg = "white",
    command = update_record,
    font = f
)

del_btn = Button(
    f1,
    text='Delete',
    bg = '#BD2A2E',
    fg = "white",
    command = deleteRow,
    font = f
)

# grid placement
cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

# Treeview
tv = ttk.Treeview(f2, columns=(1,2,3,4), show='headings', height=8)
tv.pack(side='left')

# add heading to treeview
tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="No")
tv.heading(2, text="Item Name")
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

# binding treeview
tv.bind("<ButtonRelease-1>", select_record)

# style for treeview
style = ttk.Style()
style.theme_use('default')
style.map('Treeview')

# Vertical scrollbar
scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side='right', fill='y')
tv.config(yscrollcommand=scrollbar.set)

# calling function
fetch_records()

#3 infinite loop
ws.mainloop()