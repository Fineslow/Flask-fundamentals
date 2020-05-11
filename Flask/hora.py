from flask import Flask, request, render_template, jsonify
from datetime import datetime


app = Flask(__name__)

#This gonna show us the actual time, but we need to update the page to see the actual time. 

@app.route('/')
def showActualTime():
	fecha = datetime.now()
	diccionario = {'hora': [fecha.hour, fecha.minute, fecha.second], 'fecha': [fecha.day, fecha.month, fecha.year]}
	return jsonify(diccionario)
    


if __name__ == "__main__":
    app.run()