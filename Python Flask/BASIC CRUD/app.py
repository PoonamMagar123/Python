from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'djfggfhjffffjfjhgfasbvahsdd'

userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/company"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self,  name, email, mobile, address):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address

@app.route('/')
def index():
    data_register = db.session.query(Register)
    return render_template ('index.html', data = data_register)

@app.route('/input' , methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        address = request.form['address']

        add_data = Register(name, email, mobile, address)

        db.session.add(add_data)
        db.session.commit()

        flash("Successfully add Data...!")
        return redirect (url_for('index'))
    return render_template ('input.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    data_register = Register.query.get(id)
    return render_template('edit.html', data=data_register)

@app.route('/process_edit' , methods=['GET', 'POST'])
def process_edit():
    data_register = Register.query.get(request.form.get('id'))
    
    data_register.name = request.form['name']
    data_register.email = request.form['email']
    data_register.mobile = request.form['mobile']
    data_register.address = request.form['address']

    db.session.commit()

    flash('Edit Data Success')
    return redirect (url_for('index'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    data_register = Register.query.get(id)
    db.session.delete(data_register)
    db.session.commit()
    
    flash('Deleted Data')
    return redirect (url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
