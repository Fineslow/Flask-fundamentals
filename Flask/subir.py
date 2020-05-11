from flask import Flask, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('subir.html')

@app.route('/iris', methods=['GET','POST'])
def iris():
    if request.method == 'POST':
        f = request.form['csvfile']
        iris = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                iris.append(row)
        return render_template('iris.html', iris=iris)

if __name__ == "__main__":
    app.run()