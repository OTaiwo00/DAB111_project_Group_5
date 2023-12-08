from flask import Flask, render_template, jsonify
import sqlite3
import pathlib

app = Flask(__name__)

base_path = pathlib.Path().cwd()
db_name = "breastcancer.db"
file_path = base_path / db_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    #print(file_path)
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    breastcancer_data = cursor.execute("SELECT * FROM breast_cancer LIMIT 30").fetchall()
    con.close()
    return render_template('data_page.html',breastcancer_data_data=breastcancer_data) #Here we render the template and pass the data as context

if __name__ == "__main__":
    app.run(debug=True)