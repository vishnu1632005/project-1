from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    cursor = db.cursor()
    name = request.form['name']
    email = request.form['email']
    cursor.execute("INSERT INTO mytable (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
