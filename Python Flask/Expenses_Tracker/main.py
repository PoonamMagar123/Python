import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.curser()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date)")
        self.conn.commit()
    
    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def insertRecord(self, item_name, item_price, purchase_date):

        self.cur.execute("INSERT INTO expense_record VALUES (?,?,?)", (item_name, item_price, purchase_date))
        self.conn.commit()

    def insertRecord(self, item_name, item_price, purchase_date):

        self.cur.execute("DELETE FROM expense_record WHERE rowid=? (?,?,?)", (rwid,))
        self.conn.commit()

    def updateRecord(self, item_name, item_price, purchase_date, rwid):
            self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?",
                            (item_name, item_price, purchase_date, rwid))
            self.conn.commit()

    def __del__(self):
        self.conn.close()