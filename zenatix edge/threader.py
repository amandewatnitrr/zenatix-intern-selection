import time
import pyrebase
import requests
import random
import threading, queue
import decimal
import csv
from firebase import firebase

TOKEN = "ddGzXBrit5jLqp15ssLon8oPUZs1X0IHs3HIHyEZ"  # Put your TOKEN here
DSN = 'https://bmp180-1569c.firebaseio.com/' # 'https://myapp.firebaseio.com/'
#SECRET = 'shruti7376036196' # 'secretkey'
#EMAIL ='shruti456rawal@gmail.com' # 'prateekrai266@gmail.com'
q = queue.Queue()
#authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
buffer = 0
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
  
    #temp = format(sensor.read_temperature())
    #pres = format(sensor.read_pressure())
    #oxi_level = format(95+float(decimal.Decimal(random.randrange(-85,198))/100))
    #if temp is not None and pres is not None and oxi_level is not None:  
        #str_temp = ' {0:0.2f} *C '.temp 
        #str_pres  = ' {0:0.2f} %'.pres
        #str_alti = ' {0:0.2f} m'.alti
    #    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    #    print('Pressure = {0:0.2f} KPa'.format(sensor.read_pressure()/1000))
    #    print('Oxygen Saturation = {0:0.2f} %'.format(float(oxi_level)))
    #    print('Sealevel Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    #    print("[INFO] Attemping to send data")
    #    print("[INFO] finished")
    #    print("\n")
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
                while result['status']>1:
                    bufferf(row-int(result['status']),result['status'])
                    
            data = {"timestamp":t,"sensor_data":float(k),"sensor":s}
            db.child("main_test").child("1-set").set(data)
            count = count + 1
            success = count- buffer
            time.sleep(3)
    print("Success:",success,", Buffer:",buffer)
    
update_database(count)






def bufferf(prow,stat):
    while stat>1:
        q.put(prow)
        stat = stat - 1
        prow = prow + 1
        buffer = buffer + 1
    while q.empty()==False:
        row = q.get()
        t = f'{row["Timestamp"]}'
        k = f'{row["Value"]}'
        s = f'{row["Sensor"]}'
        data = {"timestamp":t,"sensor_data":float(k),"sensor":s}
        db.child("main_test").child("1-set").set(data)
        q.task_done()
        time.sleep(5)
        