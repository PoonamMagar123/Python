from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')
 
app = Flask(__name__)
app.secrete_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin@123'
app.config['MYSQL_DB'] = 'CRUD'

@app.route()
def Index():
    cur = mysql.connection.curser()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()


if __name__ == "__main__":
    app.run(debug=True)