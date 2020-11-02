from flask import Flask, render_template, redirect, jsonify, url_for, flash, Response, send_file
import requests 
import json
import io
import pandas as pd
import xlwt

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='ezops')



@app.route('/reverse')
def reverse():  
	df = pd.read_csv('train.csv') 
	return Response((df.iloc[:,::-1]).to_csv(), mimetype = "text/csv",headers = {"Content-disposition":"attachment; filename = reverse.csv"})



@app.route('/alternate')
def alternate():
	df = pd.read_csv('train.csv')
	return Response((df.iloc[:,::2]).to_csv(), mimetype = "text/csv",headers = {"Content-disposition":"attachment; filename = alternate.csv"})



@app.route('/alpha')
def alpha():
	response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=M7HC3QRCOL3W1NXG")
	time_series = response.json()["Time Series (Daily)"]

	df = pd.DataFrame(data=time_series)

	df = (df.T)
	print (df)
	
	strIO = io.BytesIO()

	excel_writer = pd.ExcelWriter(strIO, engine="xlsxwriter")
	df.to_excel(excel_writer, sheet_name="sheet1")
	excel_writer.save()
	excel_data = strIO.getvalue()
	strIO.seek(0)
	return send_file(strIO, attachment_filename="microsoft.xlsx",as_attachment = True)





if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)