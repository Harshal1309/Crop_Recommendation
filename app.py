from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
import numpy as np
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hrjoshi@13",
  database="cropproject"
)
if mydb.is_connected():
    print("Connected to MySQL database")


app = Flask(__name__)


@app.route('/') ##, methods= ['GET', 'POST'])
def hello_world():
    return render_template('index.html')
    # if request.method == 'POST':

        # email = request.form['email']
        # N = request.form['N']
        # P = request.form['P']
        # K = request.form['K']
        # Temp = request.form['Temp']
        # Humidity = request.form('Humidity')
        # print(email, N, P, K, Temp, Humidity)
        # result = 'Grapes'
        # li.append(N, P, K, Temp, Humidity, result)
        # print(li)
        # print(result)
        # return render_template('index.html', result = result)
    

    # with open('models/model.pkl', 'rb') as f:
    #     print("Opened")
    #     model = pickle.load(f)
    #     print(model.predict(N,P,K,Temp,Humidity))


@app.route('/process_form', methods=['POST'])
def process_form():
    # Get the input values from the form
    email = request.form['email']
    N = request.form['N']
    P = request.form['P']
    K = request.form['K']
    Temp = request.form['Temp']
    Humidity = request.form['Humidity']
    pH = request.form['pH']
    Rainfall = request.form['Rainfall']
    Ex_crop = request.form['ex_crop']
    DateCreated = datetime.datetime.now()


    with open('models/randomforest.pkl', 'rb') as f:
        data = np.array([[N, P, K, Temp, Humidity, pH, Rainfall]])
        model = pickle.load(f)
        prediction = model.predict(data)
        result = prediction[0].capitalize()
        print(data, result)
        info = (email, N, P, K, Temp, Humidity, Ex_crop, result, DateCreated)
        print(info)
        mycursor = mydb.cursor()
        sql_query = "insert into cropdata (email_id, N, P, K, Temp, Humidity, Existing_Crop, Recommended_Crop, DateCreated) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        mycursor.execute(sql_query, info)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        
    return render_template('index.html', result=result)



if __name__ == "__main__": 
    app.run(debug=True)