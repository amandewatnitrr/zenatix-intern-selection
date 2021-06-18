import pyrebase
from datetime import datetime
import time
import requests
import random
import decimal
import csv
from time import strptime
from firebase import firebase

config = {
  "apiKey": "database-secret",
  "authDomain": "bmp180-1569c.firebaseapp.com",
  "databaseURL": "https://bmp180-1569c-default-rtdb.firebaseio.com",
  "storageBucket": "bmp180-1569c.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

fmt = '%Y-%m-%dT%H:%M:%S+05:30'
ts1 = datetime.strptime('2020-12-03T11:48:43+05:30',fmt)
count = 0;

def read_cloud(count,ts):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://bmp180-1569c-default-rtdb.firebaseio.com', None)
    result = firebase.get('/main_test/1-set','')
    timer = str(result['timestamp'])
    value = str(result['sensor_data'])
    sensor = str(result['sensor'])
    ts2 = datetime.strptime(timer, fmt)
    if (value == " " or (float(round((ts2-ts).total_seconds() / 60))>1)) and count != 0:
        db.child("main_test").child("1-set").child('status').set(0)
    #else:
        #db.child("main_test").child("1-set").child('status').set(random.choice([0,1]))
    data = [timer,value,sensor]
    with open('bmp_180.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print(data,float(round((ts2-ts).total_seconds() / 60)))
    time.sleep(3)
    count = count+1
    read_cloud(count,ts2)

read_cloud(count,ts1)

