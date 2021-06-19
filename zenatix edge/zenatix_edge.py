import time
import pyrebase
import requests
import random
import decimal
import csv
from firebase import firebase

TOKEN = "ddGzXBrit5jLqp15ssLon8oPUZs1X0IHs3HIHyEZ"  # Put your TOKEN here
DSN = 'https://bmp180-1569c.firebaseio.com/' # 'https://myapp.firebaseio.com/'
#SECRET = 'shruti7376036196' # 'secretkey'
#EMAIL ='shruti456rawal@gmail.com' # 'prateekrai266@gmail.com'

#authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
success = 0

config = {
  "apiKey": "database-secret",
  "authDomain": "bmp180-1569c.firebaseapp.com",
  "databaseURL": "https://bmp180-1569c-default-rtdb.firebaseio.com",
  "storageBucket": "bmp180-1569c.appspot.com"
}

count = 0

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def update_database(count):    
    buffer = 0
    with open('dataset.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            t = f'{row["Timestamp"]}'
            k = f'{row["Value"]}'
            s = f'{row["Sensor"]}'
            print(row['Value'])
            if count!=0:
                from firebase import firebase
                firebase = firebase.FirebaseApplication('https://bmp180-1569c-default-rtdb.firebaseio.com', None)
                result = firebase.get('/main_test/1-set/','')
                #if result['status']>1:
                    #buffer = buffer + int(result['status'])-1
                    
            data = {"timestamp":t,"sensor_data":float(k),"sensor":s}
            db.child("main_test").child("1-set").set(data)
            count = count + 1
            time.sleep(60)
    
update_database(count)
