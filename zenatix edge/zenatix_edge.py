import Adafruit_BMP.BMP085 as BMP085 
import time
import pyrebase
import requests
import random
import decimal
import csv
sensor = BMP085.BMP085()
from firebase import firebase

TOKEN = "ddGzXBrit5jLqp15ssLon8oPUZs1X0IHs3HIHyEZ"  # Put your TOKEN here
DSN = 'https://bmp180-1569c.firebaseio.com/' # 'https://myapp.firebaseio.com/'
#SECRET = 'shruti7376036196' # 'secretkey'
#EMAIL ='shruti456rawal@gmail.com' # 'prateekrai266@gmail.com'

#authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)

config = {
  "apiKey": "database-secret",
  "authDomain": "bmp180-1569c.firebaseapp.com",
  "databaseURL": "https://bmp180-1569c-default-rtdb.firebaseio.com",
  "storageBucket": "bmp180-1569c.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def update_database():  
  
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
            data = {"timestamp":t,"sensor_data":float(k),"sensor":s}
            db.child("main_test").child("1-set").set(data)
            time.sleep(3);
    
update_database()

